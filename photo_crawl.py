"""
Created on 2019.08.15
:author: Felix Soubelet

A simply script to run analysis and get insight on my use of equipment and settings in my practice of photography.
"""

import pyexifinfo as pyexif
import pandas as pd
from pathlib import Path
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from plotting_functions import plot_insight

RAW_FORMATS: dict = {
    "JPG": "The classic jpg file format",
    "JPEG": "Also the jpg file format",
    "3FR": "Hasselblad 3F RAW Image",
    "ARI": "ARRIRAW Image",
    "ARW": "Sony Digital Camera Image",
    "BAY": "Casio RAW Image",
    "CR2": "Canon Raw Image File",
    "CR3": "Canon Raw 3 Image File",
    "CRW": "Canon Raw CIFF Image File",
    "CS1": "CaptureShop 1-shot Raw Image",
    "CXI": "FMAT RAW Image",
    "DCR": "Kodak RAW Image File",
    "DNG": "Digital Negative Image File",
    "EIP": "Enhanced Image Package File",
    "ERF": "Epson RAW File",
    "FFF": "Hasselblad RAW Image",
    "IIQ": "Phase One RAW Image",
    "J6I": "Ricoh Camera Image File",
    "K25": "Kodak K25 Image",
    "KDC": "Kodak Photo-Enhancer File",
    "MEF": "Mamiya RAW Image",
    "MFW": "Mamiya Camera Raw File",
    "MOS": "Leaf Camera RAW File",
    "MRW": "Minolta Raw Image File",
    "NEF": "Nikon Electronic Format RAW Image",
    "NRW": "Nikon Raw Image File",
    "ORF": "Olympus RAW File",
    "PEF": "Pentax Electronic File",
    "RAF": "Fuji RAW Image File",
    "RAW": "Raw Image Data File",
    "RW2": "Panasonic RAW Image",
    "RWL": "Leica RAW Image",
    "RWZ": "Rawzor Compressed Image",
    "SR2": "Sony RAW Image",
    "SRF": "Sony RAW Image",
    "SRW": "Samsung RAW Image",
    "X3F": "SIGMA X3F Camera RAW File",
}

INTERESTING_FEATURES: list = [
    "DateTimeOriginal",
    "ExposureCompensation",
    "ExposureProgram",
    "FNumber",
    "Flash",
    "FocalLengthIn35mmFormat",
    "ISO",
    "LensMake",
    "LensModel",
    "Make",
    "MeteringMode",
    "Model",
    "ShutterSpeedValue",
    "WhiteBalance",
]


def get_exif(file_path: str) -> dict:
    """
    Returns a dict with interesting features from image EXIF.
    :param file_path: Absolute path to the file location.
    :return: a dictionary with the exif fields and value for the specific file.
    """
    return {key[5:]: value for key, value in pyexif.get_json(file_path)[0].items() if key[5:] in INTERESTING_FEATURES}


def process_files() -> pd.DataFrame:
    """
    Asks for the UNIX absolute path of the top directory where files are stored. Files can be stored in
    subdirectories, those will then be crawled recursively.
    :return: a pandas DataFrame with all interesting exif info extracted from all files.
    """
    rootpath = input("Absolute UNIX path to top directory of files location: ")
    images = []
    for extension in RAW_FORMATS.keys():
        images.extend(Path(rootpath).glob(f"**/*.{extension}"))
        images.extend(Path(rootpath).glob(f"**/*.{extension.lower()}"))
    images = sorted([str(result) for result in images])
    with Pool(cpu_count()) as pool:
        metadata = pd.DataFrame(
            list(tqdm(pool.imap_unordered(get_exif, images), desc="Scraping Images", total=len(images), unit=" Files"))
        )
        return metadata


def figure_focal_range(row: pd.Series) -> str:
    """
    Categorize the focal length value in different ranges. This is better for plotting the number of shots per focal
    length (focal range). To be applied as a lambda on a column of your DataFrame.
    :param row: a pandas Series type, should be a column of your DataFrame.
    :return:
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
        return "400mm+"


def rework_data(exif_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Formats a Dataframe with better labels and content from original. Does NOT act on the original.
    :param exif_dataframe: your pandas DataFrame containing exif information of all files.
    :return: a reworked pandas DataFrame.
    """
    temp_df = exif_dataframe.copy()
    temp_df.rename(
        {
            "ExposureCompensation": "Exposure_Compensation",
            "ExposureProgram": "Exposure_Program",
            "FNumber": "F_Number",
            "FocalLengthIn35mmFormat": "Focal_Length",
            "LensMake": "Lens_Brand",
            "LensModel": "Lens",
            "Make": "Brand",
            "MeteringMode": "Metering_Mode",
            "Model": "Camera",
            "ShutterSpeedValue": "Shutter_Speed",
            "WhiteBalance": "White_Balance",
        },
        axis="columns",
        inplace=True,
    )
    temp_df.dropna(inplace=True)
    temp_df.head()
    # Simplify the dates
    temp_df["Year"] = temp_df.DateTimeOriginal.str[:4]
    temp_df["Month"] = temp_df.DateTimeOriginal.str[5:7]
    temp_df["Day"] = temp_df.DateTimeOriginal.str[8:10]

    # Determine focal length ranges
    temp_df.Focal_Length = temp_df.Focal_Length.apply(lambda x: int(str(x[:3])))
    temp_df["Focal_Range"] = temp_df.apply(lambda row: figure_focal_range(row), axis=1)

    # Make categorical
    for col in [
        "Exposure_Compensation",
        "Exposure_Program",
        "Flash",
        "Lens_Brand",
        "Lens",
        "Brand",
        "Metering_Mode",
        "Camera",
        "Shutter_Speed",
        "White_Balance",
        "Focal_Range",
    ]:
        temp_df.loc[:, col] = temp_df.loc[:, col].astype("category")

    # Clarify some labels.
    temp_df.Lens = temp_df.Lens.cat.remove_unused_categories()
    temp_df["Metering_Mode"] = (
        temp_df["Metering_Mode"]
        .map({"Center-weighted average": "Center Weighted", "Multi-segment": "Multi Segment"})
        .fillna(temp_df["Metering_Mode"])
    )
    # Can't cover all lenses, probably unnecessary.
    temp_df["Lens"] = (
        temp_df["Lens"]
        .map(
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
        .fillna(temp_df["Lens"])
    )

    temp_df.dropna(inplace=True)
    return temp_df


def main() -> None:
    """
    Prompts for path, crawls files, extracts exif and plots insight.
    :return: nothing.
    """
    if not Path("outputs").is_dir():
        Path("outputs").mkdir()
    exif_data = process_files()
    exif_data = rework_data(exif_data)
    plot_insight(exif_data)


if __name__ == "__main__":
    main()
