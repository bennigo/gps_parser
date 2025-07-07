import gps_parser as cp


def main():
    print("TEST gps_parser")

    config = cp.ConfigParser()

    print(config.get_config("THEY", "station_name"))
    print(config.get_config("Configs", "coordfile"))

    print("get_postprocess_config_path()")
    print(config.get_postprocess_config_path())
    print("\n------- get_stations_config_path() ----------")
    print(config.get_stations_config_path())

    print('\n-------------- getStationInfo("THEY") --------------')
    print(config.getStationInfo("THEY"))

    print("from: plotVelo")
    coordfile = config.getPostprocessConfig("coordFile")
    print(coordfile)
    print("from: plateDict")
    print(config.getPostprocessConfig("plateFile"))
    print(config.getPostprocessConfig("coordFile"))
    print(config.getPostprocessConfig("detrendFile"))

    # sta_name = config.getStationInfo("THEY")  # ["station"]["name"]
    # print(sta_name)
    # Dir = config.getPostprocessConfig("totPath")
    # print(Dir)


if __name__ == "__main__":
    main()
