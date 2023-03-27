docker exec -it container_id bash

cqlsh

CREATE KEYSPACE cassandra_tutorial WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'};

USE cassandra_tutorial;

# Düzenlenecek

    CREATE TABLE energy_data (
        time timestamp,
        use_kW double,
        gen_kW double,
        house_overall_kW double,
        dishwasher_kW double,
        furnace_1_kW double,
        furnace_2_kW double,
        home_office_kW double,
        fridge_kW double,
        wine_cellar_kW double,
        garage_door_kW double,
        kitchen_12_kW double,
        kitchen_14_kW double,
        kitchen_38_kW double,
        barn_kW double,
        well_kW double,
        microwave_kW double,
        living_room_kW double,
        solar_kW double,
        temperature double,
        icon text,
        humidity double,
        visibility int,
        summary text,
        apparentTemperature double,
        pressure double,
        windSpeed double,
        cloudCover text,
        windBearing int,
        precipIntensity double,
        dewPoint double,
        precipProbability int,
        PRIMARY KEY (time)
    );




SELECT * FROM energy_data;

exit

exit
