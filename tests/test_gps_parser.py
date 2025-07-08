import gps_parser as cp


def main():
    print("TEST gps_parser")

    config = cp.ConfigParser()

    print(config.get_config("THEY", "station_name"))
    print(config.get_config("FILES", "coordFile"))

    print("get_postprocess_config_path()")
    print(config.get_postprocess_config_path())
    print("\n------- get_stations_config_path() ----------")
    print(config.get_stations_config_path())
    #
    print('\n-------------- getStationInfo("THEY") --------------')
    print(config.getStationInfo("THEY"))
    #
    print("from: plotVelo")
    coordfile = config.getPostProcessConfig("coordFile")
    print(coordfile)
    print("from: plateDict")
    print(config.getPostProcessConfig("plateFile"))
    print(config.getPostProcessConfig("coordFile"))
    print(config.getPostProcessConfig("detrendFile"))

    sta_name = config.getStationInfo("THEY")  # ["station"]["name"]
    print(sta_name)
    Dir = config.getPostProcessDir("totDir")
    print(Dir)


if __name__ == "__main__":
    main()
