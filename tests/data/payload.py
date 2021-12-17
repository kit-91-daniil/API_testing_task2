class Payload:
    CORRECT_TITLE_BODY_PAYLOAD = [("title", "body"),
                                  ("title1", "body1"),
                                  ("title2", "body2"),
                                  ("title3", "body3"),
                                  ("title", "body")]

    CORRECT_POST_IDS = [1, 2, 3, 4, 5]
    INCORRECT_POST_IDS = [102, 103, 104, 105, 106]

    CORRECT_ID_TITLE_BODY_PAYLOAD = [(1, "updated title1", "updated body1"),
                                     (2, "updated title2", "updated body2"),
                                     (3, "updated title3", "updated body3"),
                                     (4, "updated title4", "updated body4"),
                                     (5, "updated title5", "updated body5")]

    INCORRECT_ID_TITLE_BODY_PAYLOAD = [(501, "updated title1", "updated body1"),
                                       (502, "updated title2", "updated body2"),
                                       (503, "updated title3", "updated body3"),
                                       (504, "updated title4", "updated body4"),
                                       (505, "updated title5", "updated body5")]
