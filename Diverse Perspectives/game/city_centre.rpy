label city_centre:
    if by_bike:
        scene bg minnaert_bike_shed with Dissolve(0.5)
        call show_avatar
        "As you leave the KBG, you look for your bike."
    else:
        scene bg usp_bus_stop with Dissolve(0.5)
        call show_avatar
        "As you leave the KBG, you look for the bus stop."
