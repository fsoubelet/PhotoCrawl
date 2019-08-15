"""
Created on 2019.08.13
:author: Felix Soubelet

A simply script to run analysis and get insight on my use
of equipment and settings in my practice of photography.
"""

from glob import glob
from multiprocessing import Pool
import pandas as pd
from PIL import Image
from PIL import ExifTags
from tqdm import tqdm
from plotting_functions import plot_insight


INTERESTING_INFO = [
    "Make",
    "Model",
    "DateTimeOriginal",
    "FocalLengthIn35mmFilm",
    "ExposureTime",
    "FNumber",
    "ISOSpeedRatings",
    "LensMake",
    "LensModel",
]


def get_exif(file_path: str) -> dict:
    """Returns a dict with interesting features from image EXIF."""
    storage = {}
    img = Image.open(file_path)
    exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
    for key, value in exif.items():
        if key in INTERESTING_INFO:
            storage[key] = value
    return storage


def process_files() -> pd.DataFrame:
    """Extracts EXIF of all files in provided path and return a Dataframe with that data."""
    rootpath = input("Absolute UNIX path to files location: ")
    images = (
        glob(rootpath + "/**/*.jpg")
        + glob(rootpath + "/**/*.JPG")
        + glob(rootpath + "/**/*.jpeg", recursive=True)
    )
    with Pool(16) as pool:
        metadata = pd.DataFrame(
            list(
                tqdm(
                    pool.imap_unordered(get_exif, images),
                    desc="Scraping Images",
                    total=len(images),
                    unit=" Files",
                )
            )
        )
    return metadata


def figure_frange(row) -> str:
    """
    Categorize the focal length value in different ranges. This is better for plotting
    the number of shots per focal length (focal range).
    To be applied as a lambda on a row.
    """
    if row["Focal_Length"] < 10:
        return "1-9mm"
    if 10 <= row["Focal_Length"] < 16:
        return "10-15mm"
    if 16 <= row["Focal_Length"] < 23:
        return "16-23mm"
    if 24 <= row["Focal_Length"] < 70:
        return "24-70mm"
    if 70 <= row["Focal_Length"] < 200:
        return "70-200mm"
    if 200 <= row["Focal_Length"] < 400:
        return "200-400mm"
    if row["Focal_Length"] > 400:
        return "400+mm"


def rework_data(exif_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Formats the Dataframe to have better labels and content."""
    temp_df = exif_dataframe.copy()
    temp_df.rename(
        {
            "FocalLengthIn35mmFilm": "Focal_Length",
            "ISOSpeedRatings": "ISO",
            "Make": "Brand",
            "LensModel": "Lens",
            "Model": "Camera",
            "FNumber": "F_Number",
            "LensMake": "Lens_Brand",
            "ExposureTime": "Shutter_Speed",
        },
        axis="columns",
        inplace=True,
    )
    temp_df.dropna(inplace=True)

    # Simplify the dates
    temp_df["Year"] = temp_df.DateTimeOriginal.str[:4]
    temp_df["Month"] = temp_df.DateTimeOriginal.str[5:7]
    temp_df["Day"] = temp_df.DateTimeOriginal.str[8:10]
    # del temp_df["DateTimeOriginal"]

    # Get proper values for shutter speed and f-number
    temp_df.Shutter_Speed = temp_df.Shutter_Speed.apply(lambda x: "1/" + str(x[1]))
    temp_df.F_Number = temp_df.F_Number.str[0] / temp_df.F_Number.str[1]

    # Determine focal length ranges
    temp_df["Focal_Range"] = temp_df.apply(lambda row: figure_frange(row), axis=1)

    # Make categorical
    for col in ["Lens_Brand", "Lens", "Brand", "Camera", "Focal_Range", "Shutter_Speed"]:
        temp_df.loc[:, col] = temp_df.loc[:, col].astype("category")

    # Clarify lens names. Shouldn't stay here too long as I can't cover all lenses anyway.
    temp_df.Lens = temp_df.Lens.cat.remove_unused_categories()
    temp_df["Lens"] = temp_df["Lens"].map(
        {
            "XF10-24mmF4 R OIS": "XF 10-24mm f/4 R",
            "XF18-135mmF3.5-5.6R LM IOS WR": "XF 18-135mm f/3.5-5.6 R LM OIS WR",
            "XF18-55mmF2.8-4 R LM OIS": "XF 18-55mm f/2.8-4 R LM OIS",
            "XF23mmF1.4 R": "XF 23mm f/1.4 R",
            "XF50-140mmF2.8 R LM OIS WR": "XF 50-140mm f/2.8 R LM OIS WR",
            "XF50-140mmF2.8 R LM OIS WR + 1.4x": "XF 50-140mm f/2.8 R LM OIS WR + 1.4x",
            "XF55-200mmF3.5-4.8 R LM OIS": "XF 55-200mm f/3.5-4.8 R LM OIS",
            "XF56mmF1.2 R APD": "XF 56mm f/1.2 R APD",
        }
    )
    temp_df.dropna(inplace=True)
    return temp_df


def main():
    """Prompt for path, crawl files, extract exif and plot insight."""
    exif_data = process_files()
    exif_data = rework_data(exif_data)
    plot_insight(exif_data)


if __name__ == "__main__":
    main()