import configparser
import os
# import shutil


class ConfigParser:
    def __init__(self):
        # Setting up the working directories
        # self.config = configparser.ConfigParser()
        self.config = configparser.ConfigParser(
            interpolation=configparser.ExtendedInterpolation()
        )

        self.config_path = os.environ.get("GPS_CONFIG_PATH")
        if self.config_path is None:
            # [INFO:] if GPS_CONFIG_PATH is not set ~/.gpsconfig/gpsconfig as default
            home = os.path.expanduser("~")
            self.config_path = os.path.join(home, ".config", "gpsconfig")

        if not os.path.isdir(self.config_path):
            raise Exception(
                f"Directory '{self.config_path}' does not exist.\nPlease create the "
                + "directory or provide a path to the config files trough GPS_CONFIG_PATH variable\n"
                + "Make sure the relevant config files are precent in the directory.\n"
                + "you can run the script script/setup-config.sh "
                + "to create the directory and copy example files"
            )

        # print(self.config_path)
        # Reading the stations.cfg file
        self.dest_stations_config_path = os.path.join(self.config_path, "stations.cfg")
        self.config.read(self.dest_stations_config_path)

        # Reading the postprocess.cfg file
        self.dest_postprocess_config_path = os.path.join(
            self.config_path, "postprocess.cfg"
        )
        self.config.read(self.dest_postprocess_config_path)

    # Establishing the methods usable through the package to interact with the cparser module
    def get_config(self, section, option):
        """
        This function gets a configuration option from the 'stations.cfg' file.
        """
        # Getting the configuration option
        return self.config.get(section, option)

    def get_stations_config_path(self):
        """
        This function returns the path to the 'stations.cfg' file.
        """
        return self.dest_stations_config_path

    def get_postprocess_config_path(self):
        """
        This function returns the path to the 'postprocess.cfg' file.
        """

        return self.dest_postprocess_config_path

    def getStationInfo(self, station_id: str = ""):
        """
        This function gets station information from the 'stations.cfg' file.
        """
        # Read the 'station' section from the 'stations.cfg' file

        if station_id == "":
            return [
                section
                for section in self.config.sections()
                if section not in ["Configs"]
            ]
        elif self.config.has_section(station_id):
            station_info = dict(self.config.items(station_id))
            return {"station": station_info}
        else:
            raise Exception(f"Station '{station_id}' not found in 'stations.cfg' file.")

    def getPostProcessDir(self, option):
        if self.config.has_section("PATHS"):
            if self.config.has_option("PATHS", option):
                return os.path.expanduser(self.config.get("PATHS", option))
        raise Exception(
            f"Option '{option}' not found in 'Configs' section of the postprocess configuration file."
        )

    def getPostProcessConfig(self, option):
        """
        This function gets file paths from the 'postprocess.cfg' file.
        """
        # Read the 'Configs' section from the 'postprocess.cfg' file
        if self.config.has_section("FILES"):
            if self.config.has_option("FILES", option):
                return os.path.expanduser(self.config.get("FILES", option))
        raise Exception(
            f"Option '{option}' not found in 'FILES' section of the postprocess configuration file."
        )
