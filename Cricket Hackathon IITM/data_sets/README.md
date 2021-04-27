All Indian Premier League match data in CSV format
==================================================

The background
--------------

As an experiment, after being asked by a user of the site, I started
converting the YAML data provided on the site into a CSV format. That
initial version was heavily influenced by the format used by the baseball
project Retrosheet. I wasn't sure of the usefulness of my CSV format, but
nothing better was suggested so I persisted with it. Later Ashwin Raman
(https://twitter.com/AshwinRaman_) send me a detailed example of a format
he felt might work and, liking what I saw, I started to produce data in
a slightly modified version of that initial example.

This particular zip folder contains the CSV data for...
  All Indian Premier League matches
...for which we have data.

How you can help
----------------

Providing feedback on the data would be the most helpful. Tell me what you
like and what you don't. Is there anything that is in the YAML data that
you'd like to be included in the CSV? Could something be included in a better
format? General views and comments help, as well as incredibly detailed
feedback. All information is of use to me at this stage. I can only improve
the data if people tell me what does works and what doesn't. I'd like to make
the data as useful as possible but I need your help to do it. Also, which of
the 2 CSV formats do you prefer, this one or the original? Ideally I'd like
to settle on a single CSV format so what should be kept from each?

Finally, any feedback as to the licence the data should be released under
would be greatly appreciated. Licensing is a strange little world and I'd
like to choose the "right" licence. My basic criteria may be that:

  * the data should be free,
  * corrections are encouraged/required to be reported to the project,
  * derivative works are allowed,
  * you can't just take data and sell it.

Feedback, pointers, comments, etc on licensing are welcome.

The format of the data
----------------------

The first row of each CSV file contains the headers for the file, with each
subsequent row providing details on a single delivery. The headers in the
file are:

  * match_id
  * season
  * start_date
  * venue
  * innings
  * ball
  * batting_team
  * bowling_team
  * striker
  * non_striker
  * bowler
  * runs_off_bat
  * extras
  * wides
  * noballs
  * byes
  * legbyes
  * penalty
  * wicket_type
  * player_dismissed
  * other_wicket_type
  * other_player_dismissed

Most of the fields above should, hopefully, be self-explanatory, but some may
benefit from clarification...

"innings" contains the number of the innings within the match. If a match is
one that would normally have 2 innings, such as a T20 or ODI, then any innings
of more than 2 can be regarded as a super over.

"ball" is a combination of the over and delivery. For example, "0.3" represents
the 3rd ball of the 1st over.

"wides", "noballs", "byes", "legbyes", and "penalty" contain the total of each
particular type of extras, or are blank if not relevant to the delivery.

If a wicket occurred on a delivery then "wicket_type" will contain the method
of dismissal, while "player_dismissed" will indicate who was dismissed. There
is also the, admittedly remote, possibility that a second dismissal can be
recorded on the delivery (such as when a player retires on the same delivery
as another dismissal occurs). In this case "other_wicket_type" will record
the reason, while "other_player_dismissed" will show who was dismissed.

Full documentation of the CSV format will be added to the website in the
future, however if you would like to see it sooner feel free to get in
touch to let me know.

Matches included in this archive
--------------------------------

2021-04-11 - club - IPL - male - 1254060 - Kolkata Knight Riders vs Sunrisers Hyderabad
2021-04-10 - club - IPL - male - 1254059 - Chennai Super Kings vs Delhi Capitals
2021-04-09 - club - IPL - male - 1254058 - Mumbai Indians vs Royal Challengers Bangalore
2020-11-10 - club - IPL - male - 1237181 - Delhi Capitals vs Mumbai Indians
2020-11-08 - club - IPL - male - 1237180 - Delhi Capitals vs Sunrisers Hyderabad
2020-11-06 - club - IPL - male - 1237178 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2020-11-05 - club - IPL - male - 1237177 - Mumbai Indians vs Delhi Capitals
2020-11-03 - club - IPL - male - 1216495 - Mumbai Indians vs Sunrisers Hyderabad
2020-11-02 - club - IPL - male - 1216505 - Royal Challengers Bangalore vs Delhi Capitals
2020-11-01 - club - IPL - male - 1216506 - Kings XI Punjab vs Chennai Super Kings
2020-11-01 - club - IPL - male - 1216530 - Kolkata Knight Riders vs Rajasthan Royals
2020-10-31 - club - IPL - male - 1216502 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2020-10-31 - club - IPL - male - 1216535 - Delhi Capitals vs Mumbai Indians
2020-10-30 - club - IPL - male - 1216537 - Kings XI Punjab vs Rajasthan Royals
2020-10-29 - club - IPL - male - 1216536 - Kolkata Knight Riders vs Chennai Super Kings
2020-10-28 - club - IPL - male - 1216499 - Royal Challengers Bangalore vs Mumbai Indians
2020-10-27 - club - IPL - male - 1216524 - Sunrisers Hyderabad vs Delhi Capitals
2020-10-26 - club - IPL - male - 1216520 - Kolkata Knight Riders vs Kings XI Punjab
2020-10-25 - club - IPL - male - 1216541 - Mumbai Indians vs Rajasthan Royals
2020-10-25 - club - IPL - male - 1216544 - Royal Challengers Bangalore vs Chennai Super Kings
2020-10-24 - club - IPL - male - 1216497 - Kolkata Knight Riders vs Delhi Capitals
2020-10-24 - club - IPL - male - 1216498 - Kings XI Punjab vs Sunrisers Hyderabad
2020-10-23 - club - IPL - male - 1216521 - Chennai Super Kings vs Mumbai Indians
2020-10-22 - club - IPL - male - 1216518 - Rajasthan Royals vs Sunrisers Hyderabad
2020-10-21 - club - IPL - male - 1216494 - Kolkata Knight Riders vs Royal Challengers Bangalore
2020-10-20 - club - IPL - male - 1216546 - Delhi Capitals vs Kings XI Punjab
2020-10-19 - club - IPL - male - 1216533 - Chennai Super Kings vs Rajasthan Royals
2020-10-18 - club - IPL - male - 1216512 - Kolkata Knight Riders vs Sunrisers Hyderabad
2020-10-18 - club - IPL - male - 1216517 - Mumbai Indians vs Kings XI Punjab
2020-10-17 - club - IPL - male - 1216509 - Chennai Super Kings vs Delhi Capitals
2020-10-17 - club - IPL - male - 1216522 - Rajasthan Royals vs Royal Challengers Bangalore
2020-10-16 - club - IPL - male - 1216526 - Kolkata Knight Riders vs Mumbai Indians
2020-10-15 - club - IPL - male - 1216531 - Royal Challengers Bangalore vs Kings XI Punjab
2020-10-14 - club - IPL - male - 1216543 - Delhi Capitals vs Rajasthan Royals
2020-10-13 - club - IPL - male - 1216528 - Chennai Super Kings vs Sunrisers Hyderabad
2020-10-12 - club - IPL - male - 1216540 - Royal Challengers Bangalore vs Kolkata Knight Riders
2020-10-11 - club - IPL - male - 1216507 - Sunrisers Hyderabad vs Rajasthan Royals
2020-10-11 - club - IPL - male - 1216529 - Delhi Capitals vs Mumbai Indians
2020-10-10 - club - IPL - male - 1216523 - Kolkata Knight Riders vs Kings XI Punjab
2020-10-10 - club - IPL - male - 1216525 - Royal Challengers Bangalore vs Chennai Super Kings
2020-10-09 - club - IPL - male - 1216500 - Delhi Capitals vs Rajasthan Royals
2020-10-08 - club - IPL - male - 1216542 - Sunrisers Hyderabad vs Kings XI Punjab
2020-10-07 - club - IPL - male - 1216501 - Kolkata Knight Riders vs Chennai Super Kings
2020-10-06 - club - IPL - male - 1216511 - Mumbai Indians vs Rajasthan Royals
2020-10-05 - club - IPL - male - 1216519 - Delhi Capitals vs Royal Challengers Bangalore
2020-10-04 - club - IPL - male - 1216513 - Kings XI Punjab vs Chennai Super Kings
2020-10-04 - club - IPL - male - 1216538 - Mumbai Indians vs Sunrisers Hyderabad
2020-10-03 - club - IPL - male - 1216514 - Rajasthan Royals vs Royal Challengers Bangalore
2020-10-03 - club - IPL - male - 1216515 - Delhi Capitals vs Kolkata Knight Riders
2020-10-02 - club - IPL - male - 1216516 - Sunrisers Hyderabad vs Chennai Super Kings
2020-10-01 - club - IPL - male - 1216503 - Mumbai Indians vs Kings XI Punjab
2020-09-30 - club - IPL - male - 1216504 - Kolkata Knight Riders vs Rajasthan Royals
2020-09-29 - club - IPL - male - 1216532 - Sunrisers Hyderabad vs Delhi Capitals
2020-09-28 - club - IPL - male - 1216547 - Royal Challengers Bangalore vs Mumbai Indians
2020-09-27 - club - IPL - male - 1216527 - Kings XI Punjab vs Rajasthan Royals
2020-09-26 - club - IPL - male - 1216545 - Sunrisers Hyderabad vs Kolkata Knight Riders
2020-09-25 - club - IPL - male - 1216539 - Delhi Capitals vs Chennai Super Kings
2020-09-24 - club - IPL - male - 1216510 - Kings XI Punjab vs Royal Challengers Bangalore
2020-09-23 - club - IPL - male - 1216508 - Mumbai Indians vs Kolkata Knight Riders
2020-09-22 - club - IPL - male - 1216496 - Rajasthan Royals vs Chennai Super Kings
2020-09-21 - club - IPL - male - 1216534 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2020-09-20 - club - IPL - male - 1216493 - Delhi Capitals vs Kings XI Punjab
2020-09-19 - club - IPL - male - 1216492 - Mumbai Indians vs Chennai Super Kings
2019-05-12 - club - IPL - male - 1181768 - Mumbai Indians vs Chennai Super Kings
2019-05-10 - club - IPL - male - 1181767 - Chennai Super Kings vs Delhi Capitals
2019-05-08 - club - IPL - male - 1181766 - Delhi Capitals vs Sunrisers Hyderabad
2019-05-07 - club - IPL - male - 1181764 - Mumbai Indians vs Chennai Super Kings
2019-05-05 - club - IPL - male - 1178430 - Kings XI Punjab vs Chennai Super Kings
2019-05-05 - club - IPL - male - 1178431 - Mumbai Indians vs Kolkata Knight Riders
2019-05-04 - club - IPL - male - 1178428 - Delhi Capitals vs Rajasthan Royals
2019-05-04 - club - IPL - male - 1178429 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2019-05-03 - club - IPL - male - 1178427 - Kings XI Punjab vs Kolkata Knight Riders
2019-05-02 - club - IPL - male - 1178426 - Mumbai Indians vs Sunrisers Hyderabad
2019-05-01 - club - IPL - male - 1178425 - Chennai Super Kings vs Delhi Capitals
2019-04-30 - club - IPL - male - 1178424 - Royal Challengers Bangalore vs Rajasthan Royals
2019-04-29 - club - IPL - male - 1178423 - Sunrisers Hyderabad vs Kings XI Punjab
2019-04-28 - club - IPL - male - 1178421 - Delhi Capitals vs Royal Challengers Bangalore
2019-04-28 - club - IPL - male - 1178422 - Kolkata Knight Riders vs Mumbai Indians
2019-04-27 - club - IPL - male - 1178420 - Rajasthan Royals vs Sunrisers Hyderabad
2019-04-26 - club - IPL - male - 1178419 - Chennai Super Kings vs Mumbai Indians
2019-04-25 - club - IPL - male - 1178418 - Kolkata Knight Riders vs Rajasthan Royals
2019-04-24 - club - IPL - male - 1178417 - Royal Challengers Bangalore vs Kings XI Punjab
2019-04-23 - club - IPL - male - 1178416 - Chennai Super Kings vs Sunrisers Hyderabad
2019-04-22 - club - IPL - male - 1178415 - Rajasthan Royals vs Delhi Capitals
2019-04-21 - club - IPL - male - 1178413 - Sunrisers Hyderabad vs Kolkata Knight Riders
2019-04-21 - club - IPL - male - 1178414 - Royal Challengers Bangalore vs Chennai Super Kings
2019-04-20 - club - IPL - male - 1178411 - Rajasthan Royals vs Mumbai Indians
2019-04-20 - club - IPL - male - 1178412 - Delhi Capitals vs Kings XI Punjab
2019-04-19 - club - IPL - male - 1178410 - Kolkata Knight Riders vs Royal Challengers Bangalore
2019-04-18 - club - IPL - male - 1178409 - Delhi Capitals vs Mumbai Indians
2019-04-17 - club - IPL - male - 1178408 - Sunrisers Hyderabad vs Chennai Super Kings
2019-04-16 - club - IPL - male - 1178407 - Kings XI Punjab vs Rajasthan Royals
2019-04-15 - club - IPL - male - 1178406 - Mumbai Indians vs Royal Challengers Bangalore
2019-04-14 - club - IPL - male - 1178404 - Kolkata Knight Riders vs Chennai Super Kings
2019-04-14 - club - IPL - male - 1178405 - Sunrisers Hyderabad vs Delhi Capitals
2019-04-13 - club - IPL - male - 1178402 - Mumbai Indians vs Rajasthan Royals
2019-04-13 - club - IPL - male - 1178403 - Kings XI Punjab vs Royal Challengers Bangalore
2019-04-12 - club - IPL - male - 1178401 - Kolkata Knight Riders vs Delhi Capitals
2019-04-11 - club - IPL - male - 1178400 - Rajasthan Royals vs Chennai Super Kings
2019-04-10 - club - IPL - male - 1178399 - Mumbai Indians vs Kings XI Punjab
2019-04-09 - club - IPL - male - 1178398 - Chennai Super Kings vs Kolkata Knight Riders
2019-04-08 - club - IPL - male - 1178397 - Kings XI Punjab vs Sunrisers Hyderabad
2019-04-07 - club - IPL - male - 1178395 - Royal Challengers Bangalore vs Delhi Capitals
2019-04-07 - club - IPL - male - 1178396 - Rajasthan Royals vs Kolkata Knight Riders
2019-04-06 - club - IPL - male - 1178393 - Chennai Super Kings vs Kings XI Punjab
2019-04-06 - club - IPL - male - 1178394 - Sunrisers Hyderabad vs Mumbai Indians
2019-04-05 - club - IPL - male - 1175372 - Royal Challengers Bangalore vs Kolkata Knight Riders
2019-04-04 - club - IPL - male - 1175371 - Delhi Capitals vs Sunrisers Hyderabad
2019-04-03 - club - IPL - male - 1175370 - Mumbai Indians vs Chennai Super Kings
2019-04-02 - club - IPL - male - 1175369 - Rajasthan Royals vs Royal Challengers Bangalore
2019-04-01 - club - IPL - male - 1175368 - Kings XI Punjab vs Delhi Capitals
2019-03-31 - club - IPL - male - 1175366 - Sunrisers Hyderabad vs Royal Challengers Bangalore
2019-03-31 - club - IPL - male - 1175367 - Chennai Super Kings vs Rajasthan Royals
2019-03-30 - club - IPL - male - 1175364 - Kings XI Punjab vs Mumbai Indians
2019-03-30 - club - IPL - male - 1175365 - Delhi Capitals vs Kolkata Knight Riders
2019-03-29 - club - IPL - male - 1175363 - Sunrisers Hyderabad vs Rajasthan Royals
2019-03-28 - club - IPL - male - 1175362 - Royal Challengers Bangalore vs Mumbai Indians
2019-03-27 - club - IPL - male - 1175361 - Kolkata Knight Riders vs Kings XI Punjab
2019-03-26 - club - IPL - male - 1175360 - Delhi Capitals vs Chennai Super Kings
2019-03-25 - club - IPL - male - 1175359 - Rajasthan Royals vs Kings XI Punjab
2019-03-24 - club - IPL - male - 1175357 - Kolkata Knight Riders vs Sunrisers Hyderabad
2019-03-24 - club - IPL - male - 1175358 - Mumbai Indians vs Delhi Capitals
2019-03-23 - club - IPL - male - 1175356 - Chennai Super Kings vs Royal Challengers Bangalore
2018-05-27 - club - IPL - male - 1136620 - Chennai Super Kings vs Sunrisers Hyderabad
2018-05-25 - club - IPL - male - 1136619 - Kolkata Knight Riders vs Sunrisers Hyderabad
2018-05-23 - club - IPL - male - 1136618 - Kolkata Knight Riders vs Rajasthan Royals
2018-05-22 - club - IPL - male - 1136617 - Sunrisers Hyderabad vs Chennai Super Kings
2018-05-20 - club - IPL - male - 1136615 - Delhi Daredevils vs Mumbai Indians
2018-05-20 - club - IPL - male - 1136616 - Chennai Super Kings vs Kings XI Punjab
2018-05-19 - club - IPL - male - 1136613 - Rajasthan Royals vs Royal Challengers Bangalore
2018-05-19 - club - IPL - male - 1136614 - Sunrisers Hyderabad vs Kolkata Knight Riders
2018-05-18 - club - IPL - male - 1136612 - Delhi Daredevils vs Chennai Super Kings
2018-05-17 - club - IPL - male - 1136611 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2018-05-16 - club - IPL - male - 1136610 - Mumbai Indians vs Kings XI Punjab
2018-05-15 - club - IPL - male - 1136609 - Kolkata Knight Riders vs Rajasthan Royals
2018-05-14 - club - IPL - male - 1136608 - Kings XI Punjab vs Royal Challengers Bangalore
2018-05-13 - club - IPL - male - 1136606 - Chennai Super Kings vs Sunrisers Hyderabad
2018-05-13 - club - IPL - male - 1136607 - Mumbai Indians vs Rajasthan Royals
2018-05-12 - club - IPL - male - 1136604 - Kings XI Punjab vs Kolkata Knight Riders
2018-05-12 - club - IPL - male - 1136605 - Delhi Daredevils vs Royal Challengers Bangalore
2018-05-11 - club - IPL - male - 1136603 - Rajasthan Royals vs Chennai Super Kings
2018-05-10 - club - IPL - male - 1136602 - Delhi Daredevils vs Sunrisers Hyderabad
2018-05-09 - club - IPL - male - 1136601 - Kolkata Knight Riders vs Mumbai Indians
2018-05-08 - club - IPL - male - 1136600 - Rajasthan Royals vs Kings XI Punjab
2018-05-07 - club - IPL - male - 1136599 - Sunrisers Hyderabad vs Royal Challengers Bangalore
2018-05-06 - club - IPL - male - 1136597 - Mumbai Indians vs Kolkata Knight Riders
2018-05-06 - club - IPL - male - 1136598 - Kings XI Punjab vs Rajasthan Royals
2018-05-05 - club - IPL - male - 1136595 - Chennai Super Kings vs Royal Challengers Bangalore
2018-05-05 - club - IPL - male - 1136596 - Sunrisers Hyderabad vs Delhi Daredevils
2018-05-04 - club - IPL - male - 1136594 - Kings XI Punjab vs Mumbai Indians
2018-05-03 - club - IPL - male - 1136593 - Kolkata Knight Riders vs Chennai Super Kings
2018-05-02 - club - IPL - male - 1136592 - Delhi Daredevils vs Rajasthan Royals
2018-05-01 - club - IPL - male - 1136591 - Royal Challengers Bangalore vs Mumbai Indians
2018-04-30 - club - IPL - male - 1136590 - Chennai Super Kings vs Delhi Daredevils
2018-04-29 - club - IPL - male - 1136588 - Rajasthan Royals vs Sunrisers Hyderabad
2018-04-29 - club - IPL - male - 1136589 - Royal Challengers Bangalore vs Kolkata Knight Riders
2018-04-28 - club - IPL - male - 1136587 - Chennai Super Kings vs Mumbai Indians
2018-04-27 - club - IPL - male - 1136586 - Delhi Daredevils vs Kolkata Knight Riders
2018-04-26 - club - IPL - male - 1136585 - Sunrisers Hyderabad vs Kings XI Punjab
2018-04-25 - club - IPL - male - 1136584 - Royal Challengers Bangalore vs Chennai Super Kings
2018-04-24 - club - IPL - male - 1136583 - Mumbai Indians vs Sunrisers Hyderabad
2018-04-23 - club - IPL - male - 1136582 - Delhi Daredevils vs Kings XI Punjab
2018-04-22 - club - IPL - male - 1136580 - Sunrisers Hyderabad vs Chennai Super Kings
2018-04-22 - club - IPL - male - 1136581 - Rajasthan Royals vs Mumbai Indians
2018-04-21 - club - IPL - male - 1136578 - Kolkata Knight Riders vs Kings XI Punjab
2018-04-21 - club - IPL - male - 1136579 - Royal Challengers Bangalore vs Delhi Daredevils
2018-04-20 - club - IPL - male - 1136577 - Chennai Super Kings vs Rajasthan Royals
2018-04-19 - club - IPL - male - 1136576 - Kings XI Punjab vs Sunrisers Hyderabad
2018-04-18 - club - IPL - male - 1136575 - Rajasthan Royals vs Kolkata Knight Riders
2018-04-17 - club - IPL - male - 1136574 - Mumbai Indians vs Royal Challengers Bangalore
2018-04-16 - club - IPL - male - 1136573 - Kolkata Knight Riders vs Delhi Daredevils
2018-04-15 - club - IPL - male - 1136571 - Royal Challengers Bangalore vs Rajasthan Royals
2018-04-15 - club - IPL - male - 1136572 - Kings XI Punjab vs Chennai Super Kings
2018-04-14 - club - IPL - male - 1136569 - Mumbai Indians vs Delhi Daredevils
2018-04-14 - club - IPL - male - 1136570 - Kolkata Knight Riders vs Sunrisers Hyderabad
2018-04-13 - club - IPL - male - 1136568 - Royal Challengers Bangalore vs Kings XI Punjab
2018-04-12 - club - IPL - male - 1136567 - Sunrisers Hyderabad vs Mumbai Indians
2018-04-11 - club - IPL - male - 1136566 - Rajasthan Royals vs Delhi Daredevils
2018-04-10 - club - IPL - male - 1136565 - Chennai Super Kings vs Kolkata Knight Riders
2018-04-09 - club - IPL - male - 1136564 - Sunrisers Hyderabad vs Rajasthan Royals
2018-04-08 - club - IPL - male - 1136562 - Kings XI Punjab vs Delhi Daredevils
2018-04-08 - club - IPL - male - 1136563 - Kolkata Knight Riders vs Royal Challengers Bangalore
2018-04-07 - club - IPL - male - 1136561 - Mumbai Indians vs Chennai Super Kings
2017-05-21 - club - IPL - male - 1082650 - Mumbai Indians vs Rising Pune Supergiant
2017-05-19 - club - IPL - male - 1082649 - Mumbai Indians vs Kolkata Knight Riders
2017-05-17 - club - IPL - male - 1082648 - Sunrisers Hyderabad vs Kolkata Knight Riders
2017-05-16 - club - IPL - male - 1082647 - Mumbai Indians vs Rising Pune Supergiant
2017-05-14 - club - IPL - male - 1082645 - Rising Pune Supergiant vs Kings XI Punjab
2017-05-14 - club - IPL - male - 1082646 - Delhi Daredevils vs Royal Challengers Bangalore
2017-05-13 - club - IPL - male - 1082643 - Gujarat Lions vs Sunrisers Hyderabad
2017-05-13 - club - IPL - male - 1082644 - Kolkata Knight Riders vs Mumbai Indians
2017-05-12 - club - IPL - male - 1082642 - Delhi Daredevils vs Rising Pune Supergiant
2017-05-11 - club - IPL - male - 1082641 - Mumbai Indians vs Kings XI Punjab
2017-05-10 - club - IPL - male - 1082640 - Gujarat Lions vs Delhi Daredevils
2017-05-09 - club - IPL - male - 1082639 - Kings XI Punjab vs Kolkata Knight Riders
2017-05-08 - club - IPL - male - 1082638 - Sunrisers Hyderabad vs Mumbai Indians
2017-05-07 - club - IPL - male - 1082636 - Royal Challengers Bangalore vs Kolkata Knight Riders
2017-05-07 - club - IPL - male - 1082637 - Kings XI Punjab vs Gujarat Lions
2017-05-06 - club - IPL - male - 1082634 - Sunrisers Hyderabad vs Rising Pune Supergiant
2017-05-06 - club - IPL - male - 1082635 - Delhi Daredevils vs Mumbai Indians
2017-05-05 - club - IPL - male - 1082633 - Royal Challengers Bangalore vs Kings XI Punjab
2017-05-04 - club - IPL - male - 1082632 - Delhi Daredevils vs Gujarat Lions
2017-05-03 - club - IPL - male - 1082631 - Kolkata Knight Riders vs Rising Pune Supergiant
2017-05-02 - club - IPL - male - 1082630 - Delhi Daredevils vs Sunrisers Hyderabad
2017-05-01 - club - IPL - male - 1082628 - Mumbai Indians vs Royal Challengers Bangalore
2017-05-01 - club - IPL - male - 1082629 - Rising Pune Supergiant vs Gujarat Lions
2017-04-30 - club - IPL - male - 1082626 - Kings XI Punjab vs Delhi Daredevils
2017-04-30 - club - IPL - male - 1082627 - Sunrisers Hyderabad vs Kolkata Knight Riders
2017-04-29 - club - IPL - male - 1082624 - Rising Pune Supergiant vs Royal Challengers Bangalore
2017-04-29 - club - IPL - male - 1082625 - Gujarat Lions vs Mumbai Indians
2017-04-28 - club - IPL - male - 1082622 - Kolkata Knight Riders vs Delhi Daredevils
2017-04-28 - club - IPL - male - 1082623 - Kings XI Punjab vs Sunrisers Hyderabad
2017-04-27 - club - IPL - male - 1082621 - Royal Challengers Bangalore vs Gujarat Lions
2017-04-26 - club - IPL - male - 1082620 - Rising Pune Supergiant vs Kolkata Knight Riders
2017-04-24 - club - IPL - male - 1082618 - Mumbai Indians vs Rising Pune Supergiant
2017-04-23 - club - IPL - male - 1082616 - Gujarat Lions vs Kings XI Punjab
2017-04-23 - club - IPL - male - 1082617 - Kolkata Knight Riders vs Royal Challengers Bangalore
2017-04-22 - club - IPL - male - 1082614 - Mumbai Indians vs Delhi Daredevils
2017-04-22 - club - IPL - male - 1082615 - Rising Pune Supergiant vs Sunrisers Hyderabad
2017-04-21 - club - IPL - male - 1082613 - Kolkata Knight Riders vs Gujarat Lions
2017-04-20 - club - IPL - male - 1082612 - Kings XI Punjab vs Mumbai Indians
2017-04-19 - club - IPL - male - 1082611 - Sunrisers Hyderabad vs Delhi Daredevils
2017-04-18 - club - IPL - male - 1082610 - Gujarat Lions vs Royal Challengers Bangalore
2017-04-17 - club - IPL - male - 1082608 - Delhi Daredevils vs Kolkata Knight Riders
2017-04-17 - club - IPL - male - 1082609 - Sunrisers Hyderabad vs Kings XI Punjab
2017-04-16 - club - IPL - male - 1082606 - Mumbai Indians vs Gujarat Lions
2017-04-16 - club - IPL - male - 1082607 - Royal Challengers Bangalore vs Rising Pune Supergiant
2017-04-15 - club - IPL - male - 1082604 - Kolkata Knight Riders vs Sunrisers Hyderabad
2017-04-15 - club - IPL - male - 1082605 - Delhi Daredevils vs Kings XI Punjab
2017-04-14 - club - IPL - male - 1082602 - Royal Challengers Bangalore vs Mumbai Indians
2017-04-14 - club - IPL - male - 1082603 - Gujarat Lions vs Rising Pune Supergiant
2017-04-13 - club - IPL - male - 1082601 - Kolkata Knight Riders vs Kings XI Punjab
2017-04-12 - club - IPL - male - 1082600 - Mumbai Indians vs Sunrisers Hyderabad
2017-04-11 - club - IPL - male - 1082599 - Rising Pune Supergiant vs Delhi Daredevils
2017-04-10 - club - IPL - male - 1082598 - Kings XI Punjab vs Royal Challengers Bangalore
2017-04-09 - club - IPL - male - 1082596 - Sunrisers Hyderabad vs Gujarat Lions
2017-04-09 - club - IPL - male - 1082597 - Mumbai Indians vs Kolkata Knight Riders
2017-04-08 - club - IPL - male - 1082594 - Kings XI Punjab vs Rising Pune Supergiant
2017-04-08 - club - IPL - male - 1082595 - Royal Challengers Bangalore vs Delhi Daredevils
2017-04-07 - club - IPL - male - 1082593 - Gujarat Lions vs Kolkata Knight Riders
2017-04-06 - club - IPL - male - 1082592 - Rising Pune Supergiant vs Mumbai Indians
2017-04-05 - club - IPL - male - 1082591 - Sunrisers Hyderabad vs Royal Challengers Bangalore
2016-05-29 - club - IPL - male - 981019 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2016-05-27 - club - IPL - male - 981017 - Gujarat Lions vs Sunrisers Hyderabad
2016-05-25 - club - IPL - male - 981015 - Sunrisers Hyderabad vs Kolkata Knight Riders
2016-05-24 - club - IPL - male - 981013 - Gujarat Lions vs Royal Challengers Bangalore
2016-05-22 - club - IPL - male - 981009 - Kolkata Knight Riders vs Sunrisers Hyderabad
2016-05-22 - club - IPL - male - 981011 - Delhi Daredevils vs Royal Challengers Bangalore
2016-05-21 - club - IPL - male - 981005 - Rising Pune Supergiants vs Kings XI Punjab
2016-05-21 - club - IPL - male - 981007 - Gujarat Lions vs Mumbai Indians
2016-05-20 - club - IPL - male - 981003 - Delhi Daredevils vs Sunrisers Hyderabad
2016-05-19 - club - IPL - male - 981001 - Gujarat Lions vs Kolkata Knight Riders
2016-05-18 - club - IPL - male - 980999 - Royal Challengers Bangalore vs Kings XI Punjab
2016-05-17 - club - IPL - male - 980997 - Rising Pune Supergiants vs Delhi Daredevils
2016-05-16 - club - IPL - male - 980995 - Kolkata Knight Riders vs Royal Challengers Bangalore
2016-05-15 - club - IPL - male - 980991 - Kings XI Punjab vs Sunrisers Hyderabad
2016-05-15 - club - IPL - male - 980993 - Mumbai Indians vs Delhi Daredevils
2016-05-14 - club - IPL - male - 980987 - Royal Challengers Bangalore vs Gujarat Lions
2016-05-14 - club - IPL - male - 980989 - Kolkata Knight Riders vs Rising Pune Supergiants
2016-05-13 - club - IPL - male - 980985 - Mumbai Indians vs Kings XI Punjab
2016-05-12 - club - IPL - male - 980983 - Sunrisers Hyderabad vs Delhi Daredevils
2016-05-11 - club - IPL - male - 980981 - Royal Challengers Bangalore vs Mumbai Indians
2016-05-10 - club - IPL - male - 980979 - Rising Pune Supergiants vs Sunrisers Hyderabad
2016-05-09 - club - IPL - male - 980977 - Kings XI Punjab vs Royal Challengers Bangalore
2016-05-08 - club - IPL - male - 980973 - Mumbai Indians vs Sunrisers Hyderabad
2016-05-08 - club - IPL - male - 980975 - Kolkata Knight Riders vs Gujarat Lions
2016-05-07 - club - IPL - male - 980969 - Royal Challengers Bangalore vs Rising Pune Supergiants
2016-05-07 - club - IPL - male - 980971 - Kings XI Punjab vs Delhi Daredevils
2016-05-06 - club - IPL - male - 980967 - Sunrisers Hyderabad vs Gujarat Lions
2016-05-05 - club - IPL - male - 980965 - Delhi Daredevils vs Rising Pune Supergiants
2016-05-04 - club - IPL - male - 980963 - Kolkata Knight Riders vs Kings XI Punjab
2016-05-03 - club - IPL - male - 980961 - Gujarat Lions vs Delhi Daredevils
2016-05-02 - club - IPL - male - 980959 - Royal Challengers Bangalore vs Kolkata Knight Riders
2016-05-01 - club - IPL - male - 980955 - Gujarat Lions vs Kings XI Punjab
2016-05-01 - club - IPL - male - 980957 - Rising Pune Supergiants vs Mumbai Indians
2016-04-30 - club - IPL - male - 980951 - Delhi Daredevils vs Kolkata Knight Riders
2016-04-30 - club - IPL - male - 980953 - Sunrisers Hyderabad vs Royal Challengers Bangalore
2016-04-29 - club - IPL - male - 980949 - Rising Pune Supergiants vs Gujarat Lions
2016-04-28 - club - IPL - male - 980947 - Mumbai Indians vs Kolkata Knight Riders
2016-04-27 - club - IPL - male - 980945 - Delhi Daredevils vs Gujarat Lions
2016-04-26 - club - IPL - male - 980943 - Sunrisers Hyderabad vs Rising Pune Supergiants
2016-04-25 - club - IPL - male - 980941 - Kings XI Punjab vs Mumbai Indians
2016-04-24 - club - IPL - male - 980937 - Gujarat Lions vs Royal Challengers Bangalore
2016-04-24 - club - IPL - male - 980939 - Rising Pune Supergiants vs Kolkata Knight Riders
2016-04-23 - club - IPL - male - 980933 - Delhi Daredevils vs Mumbai Indians
2016-04-23 - club - IPL - male - 980935 - Sunrisers Hyderabad vs Kings XI Punjab
2016-04-22 - club - IPL - male - 980931 - Rising Pune Supergiants vs Royal Challengers Bangalore
2016-04-21 - club - IPL - male - 980929 - Gujarat Lions vs Sunrisers Hyderabad
2016-04-20 - club - IPL - male - 980927 - Mumbai Indians vs Royal Challengers Bangalore
2016-04-19 - club - IPL - male - 980925 - Kings XI Punjab vs Kolkata Knight Riders
2016-04-18 - club - IPL - male - 980923 - Sunrisers Hyderabad vs Mumbai Indians
2016-04-17 - club - IPL - male - 980919 - Kings XI Punjab vs Rising Pune Supergiants
2016-04-17 - club - IPL - male - 980921 - Royal Challengers Bangalore vs Delhi Daredevils
2016-04-16 - club - IPL - male - 980915 - Sunrisers Hyderabad vs Kolkata Knight Riders
2016-04-16 - club - IPL - male - 980917 - Mumbai Indians vs Gujarat Lions
2016-04-15 - club - IPL - male - 980913 - Delhi Daredevils vs Kings XI Punjab
2016-04-14 - club - IPL - male - 980911 - Gujarat Lions vs Rising Pune Supergiants
2016-04-13 - club - IPL - male - 980909 - Kolkata Knight Riders vs Mumbai Indians
2016-04-12 - club - IPL - male - 980907 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2016-04-11 - club - IPL - male - 980905 - Kings XI Punjab vs Gujarat Lions
2016-04-10 - club - IPL - male - 980903 - Kolkata Knight Riders vs Delhi Daredevils
2016-04-09 - club - IPL - male - 980901 - Mumbai Indians vs Rising Pune Supergiants
2015-05-24 - club - IPL - male - 829823 - Mumbai Indians vs Chennai Super Kings
2015-05-22 - club - IPL - male - 829821 - Chennai Super Kings vs Royal Challengers Bangalore
2015-05-20 - club - IPL - male - 829819 - Royal Challengers Bangalore vs Rajasthan Royals
2015-05-19 - club - IPL - male - 829817 - Chennai Super Kings vs Mumbai Indians
2015-05-17 - club - IPL - male - 829813 - Royal Challengers Bangalore vs Delhi Daredevils
2015-05-17 - club - IPL - male - 829815 - Sunrisers Hyderabad vs Mumbai Indians
2015-05-16 - club - IPL - male - 829809 - Kings XI Punjab vs Chennai Super Kings
2015-05-16 - club - IPL - male - 829811 - Rajasthan Royals vs Kolkata Knight Riders
2015-05-15 - club - IPL - male - 829807 - Sunrisers Hyderabad vs Royal Challengers Bangalore
2015-05-14 - club - IPL - male - 829805 - Mumbai Indians vs Kolkata Knight Riders
2015-05-13 - club - IPL - male - 829803 - Kings XI Punjab vs Royal Challengers Bangalore
2015-05-12 - club - IPL - male - 829801 - Delhi Daredevils vs Chennai Super Kings
2015-05-11 - club - IPL - male - 829799 - Sunrisers Hyderabad vs Kings XI Punjab
2015-05-10 - club - IPL - male - 829795 - Mumbai Indians vs Royal Challengers Bangalore
2015-05-10 - club - IPL - male - 829797 - Chennai Super Kings vs Rajasthan Royals
2015-05-09 - club - IPL - male - 829791 - Kolkata Knight Riders vs Kings XI Punjab
2015-05-09 - club - IPL - male - 829793 - Delhi Daredevils vs Sunrisers Hyderabad
2015-05-08 - club - IPL - male - 829789 - Chennai Super Kings vs Mumbai Indians
2015-05-07 - club - IPL - male - 829761 - Kolkata Knight Riders vs Delhi Daredevils
2015-05-07 - club - IPL - male - 829787 - Rajasthan Royals vs Sunrisers Hyderabad
2015-05-06 - club - IPL - male - 829785 - Royal Challengers Bangalore vs Kings XI Punjab
2015-05-05 - club - IPL - male - 829783 - Mumbai Indians vs Delhi Daredevils
2015-05-04 - club - IPL - male - 829779 - Chennai Super Kings vs Royal Challengers Bangalore
2015-05-04 - club - IPL - male - 829781 - Kolkata Knight Riders vs Sunrisers Hyderabad
2015-05-03 - club - IPL - male - 829775 - Kings XI Punjab vs Mumbai Indians
2015-05-03 - club - IPL - male - 829777 - Rajasthan Royals vs Delhi Daredevils
2015-05-02 - club - IPL - male - 829771 - Royal Challengers Bangalore vs Kolkata Knight Riders
2015-05-02 - club - IPL - male - 829773 - Sunrisers Hyderabad vs Chennai Super Kings
2015-05-01 - club - IPL - male - 829767 - Delhi Daredevils vs Kings XI Punjab
2015-05-01 - club - IPL - male - 829769 - Mumbai Indians vs Rajasthan Royals
2015-04-30 - club - IPL - male - 829723 - Kolkata Knight Riders vs Chennai Super Kings
2015-04-29 - club - IPL - male - 829763 - Royal Challengers Bangalore vs Rajasthan Royals
2015-04-28 - club - IPL - male - 829765 - Chennai Super Kings vs Kolkata Knight Riders
2015-04-27 - club - IPL - male - 829759 - Kings XI Punjab vs Sunrisers Hyderabad
2015-04-26 - club - IPL - male - 829757 - Delhi Daredevils vs Royal Challengers Bangalore
2015-04-25 - club - IPL - male - 829751 - Mumbai Indians vs Sunrisers Hyderabad
2015-04-25 - club - IPL - male - 829753 - Chennai Super Kings vs Kings XI Punjab
2015-04-24 - club - IPL - male - 829749 - Rajasthan Royals vs Royal Challengers Bangalore
2015-04-23 - club - IPL - male - 829747 - Delhi Daredevils vs Mumbai Indians
2015-04-22 - club - IPL - male - 829743 - Sunrisers Hyderabad vs Kolkata Knight Riders
2015-04-22 - club - IPL - male - 829745 - Royal Challengers Bangalore vs Chennai Super Kings
2015-04-21 - club - IPL - male - 829741 - Rajasthan Royals vs Kings XI Punjab
2015-04-20 - club - IPL - male - 829739 - Delhi Daredevils vs Kolkata Knight Riders
2015-04-19 - club - IPL - male - 829735 - Rajasthan Royals vs Chennai Super Kings
2015-04-19 - club - IPL - male - 829737 - Royal Challengers Bangalore vs Mumbai Indians
2015-04-18 - club - IPL - male - 829731 - Sunrisers Hyderabad vs Delhi Daredevils
2015-04-18 - club - IPL - male - 829733 - Kings XI Punjab vs Kolkata Knight Riders
2015-04-17 - club - IPL - male - 829729 - Mumbai Indians vs Chennai Super Kings
2015-04-16 - club - IPL - male - 829727 - Sunrisers Hyderabad vs Rajasthan Royals
2015-04-15 - club - IPL - male - 829725 - Kings XI Punjab vs Delhi Daredevils
2015-04-14 - club - IPL - male - 829721 - Rajasthan Royals vs Mumbai Indians
2015-04-13 - club - IPL - male - 829719 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2015-04-12 - club - IPL - male - 829715 - Delhi Daredevils vs Rajasthan Royals
2015-04-12 - club - IPL - male - 829717 - Mumbai Indians vs Kings XI Punjab
2015-04-11 - club - IPL - male - 829711 - Chennai Super Kings vs Sunrisers Hyderabad
2015-04-11 - club - IPL - male - 829713 - Kolkata Knight Riders vs Royal Challengers Bangalore
2015-04-10 - club - IPL - male - 829709 - Kings XI Punjab vs Rajasthan Royals
2015-04-09 - club - IPL - male - 829707 - Chennai Super Kings vs Delhi Daredevils
2015-04-08 - club - IPL - male - 829705 - Kolkata Knight Riders vs Mumbai Indians
2014-06-01 - club - IPL - male - 734049 - Kolkata Knight Riders vs Kings XI Punjab
2014-05-30 - club - IPL - male - 734047 - Chennai Super Kings vs Kings XI Punjab
2014-05-28 - club - IPL - male - 734045 - Chennai Super Kings vs Mumbai Indians
2014-05-27 - club - IPL - male - 734043 - Kings XI Punjab vs Kolkata Knight Riders
2014-05-25 - club - IPL - male - 734039 - Kings XI Punjab vs Delhi Daredevils
2014-05-25 - club - IPL - male - 734041 - Mumbai Indians vs Rajasthan Royals
2014-05-24 - club - IPL - male - 734035 - Royal Challengers Bangalore vs Chennai Super Kings
2014-05-24 - club - IPL - male - 734037 - Kolkata Knight Riders vs Sunrisers Hyderabad
2014-05-23 - club - IPL - male - 734031 - Mumbai Indians vs Delhi Daredevils
2014-05-23 - club - IPL - male - 734033 - Kings XI Punjab vs Rajasthan Royals
2014-05-22 - club - IPL - male - 734027 - Kolkata Knight Riders vs Royal Challengers Bangalore
2014-05-22 - club - IPL - male - 734029 - Chennai Super Kings vs Sunrisers Hyderabad
2014-05-21 - club - IPL - male - 734025 - Kings XI Punjab vs Mumbai Indians
2014-05-20 - club - IPL - male - 734021 - Sunrisers Hyderabad vs Royal Challengers Bangalore
2014-05-20 - club - IPL - male - 734023 - Kolkata Knight Riders vs Chennai Super Kings
2014-05-19 - club - IPL - male - 734017 - Rajasthan Royals vs Mumbai Indians
2014-05-19 - club - IPL - male - 734019 - Delhi Daredevils vs Kings XI Punjab
2014-05-18 - club - IPL - male - 734013 - Chennai Super Kings vs Royal Challengers Bangalore
2014-05-18 - club - IPL - male - 734015 - Sunrisers Hyderabad vs Kolkata Knight Riders
2014-05-15 - club - IPL - male - 734011 - Rajasthan Royals vs Delhi Daredevils
2014-05-14 - club - IPL - male - 734007 - Sunrisers Hyderabad vs Kings XI Punjab
2014-05-14 - club - IPL - male - 734009 - Kolkata Knight Riders vs Mumbai Indians
2014-05-13 - club - IPL - male - 734003 - Chennai Super Kings vs Rajasthan Royals
2014-05-13 - club - IPL - male - 734005 - Royal Challengers Bangalore vs Delhi Daredevils
2014-05-12 - club - IPL - male - 734001 - Sunrisers Hyderabad vs Mumbai Indians
2014-05-11 - club - IPL - male - 733997 - Kings XI Punjab vs Kolkata Knight Riders
2014-05-11 - club - IPL - male - 733999 - Royal Challengers Bangalore vs Rajasthan Royals
2014-05-10 - club - IPL - male - 733993 - Delhi Daredevils vs Sunrisers Hyderabad
2014-05-10 - club - IPL - male - 733995 - Mumbai Indians vs Chennai Super Kings
2014-05-09 - club - IPL - male - 733991 - Royal Challengers Bangalore vs Kings XI Punjab
2014-05-08 - club - IPL - male - 733989 - Rajasthan Royals vs Sunrisers Hyderabad
2014-05-07 - club - IPL - male - 733985 - Delhi Daredevils vs Kolkata Knight Riders
2014-05-07 - club - IPL - male - 733987 - Kings XI Punjab vs Chennai Super Kings
2014-05-06 - club - IPL - male - 733983 - Mumbai Indians vs Royal Challengers Bangalore
2014-05-05 - club - IPL - male - 733979 - Rajasthan Royals vs Kolkata Knight Riders
2014-05-05 - club - IPL - male - 733981 - Delhi Daredevils vs Chennai Super Kings
2014-05-04 - club - IPL - male - 733977 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2014-05-03 - club - IPL - male - 733973 - Mumbai Indians vs Kings XI Punjab
2014-05-03 - club - IPL - male - 733975 - Delhi Daredevils vs Rajasthan Royals
2014-05-02 - club - IPL - male - 733971 - Chennai Super Kings vs Kolkata Knight Riders
2014-04-30 - club - IPL - male - 729317 - Mumbai Indians vs Sunrisers Hyderabad
2014-04-29 - club - IPL - male - 729315 - Kolkata Knight Riders vs Rajasthan Royals
2014-04-28 - club - IPL - male - 729313 - Kings XI Punjab vs Royal Challengers Bangalore
2014-04-27 - club - IPL - male - 729309 - Delhi Daredevils vs Mumbai Indians
2014-04-27 - club - IPL - male - 729311 - Sunrisers Hyderabad vs Chennai Super Kings
2014-04-26 - club - IPL - male - 729305 - Rajasthan Royals vs Royal Challengers Bangalore
2014-04-26 - club - IPL - male - 729307 - Kolkata Knight Riders vs Kings XI Punjab
2014-04-25 - club - IPL - male - 729301 - Sunrisers Hyderabad vs Delhi Daredevils
2014-04-25 - club - IPL - male - 729303 - Chennai Super Kings vs Mumbai Indians
2014-04-24 - club - IPL - male - 729299 - Royal Challengers Bangalore vs Kolkata Knight Riders
2014-04-23 - club - IPL - male - 729297 - Rajasthan Royals vs Chennai Super Kings
2014-04-22 - club - IPL - male - 729295 - Kings XI Punjab vs Sunrisers Hyderabad
2014-04-21 - club - IPL - male - 729293 - Chennai Super Kings vs Delhi Daredevils
2014-04-20 - club - IPL - male - 729291 - Rajasthan Royals vs Kings XI Punjab
2014-04-19 - club - IPL - male - 729287 - Royal Challengers Bangalore vs Mumbai Indians
2014-04-19 - club - IPL - male - 729289 - Kolkata Knight Riders vs Delhi Daredevils
2014-04-18 - club - IPL - male - 729283 - Chennai Super Kings vs Kings XI Punjab
2014-04-18 - club - IPL - male - 729285 - Sunrisers Hyderabad vs Rajasthan Royals
2014-04-17 - club - IPL - male - 729281 - Delhi Daredevils vs Royal Challengers Bangalore
2014-04-16 - club - IPL - male - 729279 - Mumbai Indians vs Kolkata Knight Riders
2013-05-26 - club - IPL - male - 598073 - Chennai Super Kings vs Mumbai Indians
2013-05-24 - club - IPL - male - 598072 - Mumbai Indians vs Rajasthan Royals
2013-05-22 - club - IPL - male - 598071 - Rajasthan Royals vs Sunrisers Hyderabad
2013-05-21 - club - IPL - male - 598070 - Chennai Super Kings vs Mumbai Indians
2013-05-19 - club - IPL - male - 598067 - Pune Warriors vs Delhi Daredevils
2013-05-19 - club - IPL - male - 598069 - Sunrisers Hyderabad vs Kolkata Knight Riders
2013-05-18 - club - IPL - male - 598066 - Kings XI Punjab vs Mumbai Indians
2013-05-18 - club - IPL - male - 598068 - Royal Challengers Bangalore vs Chennai Super Kings
2013-05-17 - club - IPL - male - 598065 - Sunrisers Hyderabad vs Rajasthan Royals
2013-05-16 - club - IPL - male - 598028 - Kings XI Punjab vs Delhi Daredevils
2013-05-15 - club - IPL - male - 598061 - Kolkata Knight Riders vs Pune Warriors
2013-05-15 - club - IPL - male - 598063 - Mumbai Indians vs Rajasthan Royals
2013-05-14 - club - IPL - male - 598045 - Royal Challengers Bangalore vs Kings XI Punjab
2013-05-14 - club - IPL - male - 598062 - Chennai Super Kings vs Delhi Daredevils
2013-05-13 - club - IPL - male - 598060 - Mumbai Indians vs Sunrisers Hyderabad
2013-05-12 - club - IPL - male - 598057 - Kolkata Knight Riders vs Royal Challengers Bangalore
2013-05-12 - club - IPL - male - 598058 - Rajasthan Royals vs Chennai Super Kings
2013-05-11 - club - IPL - male - 598055 - Pune Warriors vs Mumbai Indians
2013-05-11 - club - IPL - male - 598056 - Kings XI Punjab vs Sunrisers Hyderabad
2013-05-10 - club - IPL - male - 598054 - Delhi Daredevils vs Royal Challengers Bangalore
2013-05-09 - club - IPL - male - 598052 - Kings XI Punjab vs Rajasthan Royals
2013-05-09 - club - IPL - male - 598053 - Pune Warriors vs Kolkata Knight Riders
2013-05-08 - club - IPL - male - 598051 - Sunrisers Hyderabad vs Chennai Super Kings
2013-05-07 - club - IPL - male - 598049 - Rajasthan Royals vs Delhi Daredevils
2013-05-07 - club - IPL - male - 598050 - Mumbai Indians vs Kolkata Knight Riders
2013-05-06 - club - IPL - male - 598064 - Kings XI Punjab vs Royal Challengers Bangalore
2013-05-05 - club - IPL - male - 598046 - Mumbai Indians vs Chennai Super Kings
2013-05-05 - club - IPL - male - 598047 - Rajasthan Royals vs Pune Warriors
2013-05-04 - club - IPL - male - 598044 - Sunrisers Hyderabad vs Delhi Daredevils
2013-05-03 - club - IPL - male - 598043 - Kolkata Knight Riders vs Rajasthan Royals
2013-05-02 - club - IPL - male - 598041 - Chennai Super Kings vs Kings XI Punjab
2013-05-02 - club - IPL - male - 598042 - Pune Warriors vs Royal Challengers Bangalore
2013-05-01 - club - IPL - male - 598039 - Sunrisers Hyderabad vs Mumbai Indians
2013-05-01 - club - IPL - male - 598040 - Delhi Daredevils vs Kolkata Knight Riders
2013-04-30 - club - IPL - male - 598038 - Pune Warriors vs Chennai Super Kings
2013-04-29 - club - IPL - male - 598036 - Rajasthan Royals vs Royal Challengers Bangalore
2013-04-29 - club - IPL - male - 598037 - Mumbai Indians vs Kings XI Punjab
2013-04-28 - club - IPL - male - 598034 - Chennai Super Kings vs Kolkata Knight Riders
2013-04-28 - club - IPL - male - 598035 - Delhi Daredevils vs Pune Warriors
2013-04-27 - club - IPL - male - 598032 - Rajasthan Royals vs Sunrisers Hyderabad
2013-04-27 - club - IPL - male - 598033 - Mumbai Indians vs Royal Challengers Bangalore
2013-04-26 - club - IPL - male - 598031 - Kolkata Knight Riders vs Kings XI Punjab
2013-04-25 - club - IPL - male - 598030 - Chennai Super Kings vs Sunrisers Hyderabad
2013-04-24 - club - IPL - male - 598029 - Kolkata Knight Riders vs Mumbai Indians
2013-04-23 - club - IPL - male - 598027 - Royal Challengers Bangalore vs Pune Warriors
2013-04-23 - club - IPL - male - 598059 - Delhi Daredevils vs Kings XI Punjab
2013-04-22 - club - IPL - male - 598026 - Chennai Super Kings vs Rajasthan Royals
2013-04-21 - club - IPL - male - 598024 - Delhi Daredevils vs Mumbai Indians
2013-04-21 - club - IPL - male - 598025 - Kings XI Punjab vs Pune Warriors
2013-04-20 - club - IPL - male - 598022 - Kolkata Knight Riders vs Chennai Super Kings
2013-04-20 - club - IPL - male - 598023 - Royal Challengers Bangalore vs Rajasthan Royals
2013-04-19 - club - IPL - male - 598021 - Sunrisers Hyderabad vs Kings XI Punjab
2013-04-18 - club - IPL - male - 598020 - Delhi Daredevils vs Chennai Super Kings
2013-04-17 - club - IPL - male - 598018 - Pune Warriors vs Sunrisers Hyderabad
2013-04-17 - club - IPL - male - 598019 - Rajasthan Royals vs Mumbai Indians
2013-04-16 - club - IPL - male - 598016 - Kings XI Punjab vs Kolkata Knight Riders
2013-04-16 - club - IPL - male - 598017 - Royal Challengers Bangalore vs Delhi Daredevils
2013-04-15 - club - IPL - male - 598015 - Chennai Super Kings vs Pune Warriors
2013-04-14 - club - IPL - male - 598013 - Kolkata Knight Riders vs Sunrisers Hyderabad
2013-04-14 - club - IPL - male - 598014 - Rajasthan Royals vs Kings XI Punjab
2013-04-13 - club - IPL - male - 598011 - Mumbai Indians vs Pune Warriors
2013-04-13 - club - IPL - male - 598012 - Chennai Super Kings vs Royal Challengers Bangalore
2013-04-12 - club - IPL - male - 598010 - Delhi Daredevils vs Sunrisers Hyderabad
2013-04-11 - club - IPL - male - 598008 - Royal Challengers Bangalore vs Kolkata Knight Riders
2013-04-11 - club - IPL - male - 598009 - Pune Warriors vs Rajasthan Royals
2013-04-10 - club - IPL - male - 598007 - Kings XI Punjab vs Chennai Super Kings
2013-04-09 - club - IPL - male - 598006 - Mumbai Indians vs Delhi Daredevils
2013-04-09 - club - IPL - male - 598048 - Royal Challengers Bangalore vs Sunrisers Hyderabad
2013-04-08 - club - IPL - male - 598005 - Rajasthan Royals vs Kolkata Knight Riders
2013-04-07 - club - IPL - male - 598003 - Pune Warriors vs Kings XI Punjab
2013-04-07 - club - IPL - male - 598004 - Sunrisers Hyderabad vs Royal Challengers Bangalore
2013-04-06 - club - IPL - male - 598001 - Delhi Daredevils vs Rajasthan Royals
2013-04-06 - club - IPL - male - 598002 - Chennai Super Kings vs Mumbai Indians
2013-04-05 - club - IPL - male - 598000 - Sunrisers Hyderabad vs Pune Warriors
2013-04-04 - club - IPL - male - 597999 - Royal Challengers Bangalore vs Mumbai Indians
2013-04-03 - club - IPL - male - 597998 - Kolkata Knight Riders vs Delhi Daredevils
2012-05-27 - club - IPL - male - 548381 - Kolkata Knight Riders vs Chennai Super Kings
2012-05-25 - club - IPL - male - 548380 - Delhi Daredevils vs Chennai Super Kings
2012-05-23 - club - IPL - male - 548379 - Chennai Super Kings vs Mumbai Indians
2012-05-22 - club - IPL - male - 548378 - Delhi Daredevils vs Kolkata Knight Riders
2012-05-20 - club - IPL - male - 548376 - Deccan Chargers vs Royal Challengers Bangalore
2012-05-20 - club - IPL - male - 548377 - Rajasthan Royals vs Mumbai Indians
2012-05-19 - club - IPL - male - 548374 - Kings XI Punjab vs Delhi Daredevils
2012-05-19 - club - IPL - male - 548375 - Pune Warriors vs Kolkata Knight Riders
2012-05-18 - club - IPL - male - 548373 - Deccan Chargers vs Rajasthan Royals
2012-05-17 - club - IPL - male - 548371 - Kings XI Punjab vs Chennai Super Kings
2012-05-17 - club - IPL - male - 548372 - Delhi Daredevils vs Royal Challengers Bangalore
2012-05-16 - club - IPL - male - 548370 - Mumbai Indians vs Kolkata Knight Riders
2012-05-15 - club - IPL - male - 548369 - Delhi Daredevils vs Kings XI Punjab
2012-05-14 - club - IPL - male - 548367 - Royal Challengers Bangalore vs Mumbai Indians
2012-05-14 - club - IPL - male - 548368 - Kolkata Knight Riders vs Chennai Super Kings
2012-05-13 - club - IPL - male - 548365 - Rajasthan Royals vs Pune Warriors
2012-05-13 - club - IPL - male - 548366 - Kings XI Punjab vs Deccan Chargers
2012-05-12 - club - IPL - male - 548363 - Kolkata Knight Riders vs Mumbai Indians
2012-05-12 - club - IPL - male - 548364 - Chennai Super Kings vs Delhi Daredevils
2012-05-11 - club - IPL - male - 548362 - Pune Warriors vs Royal Challengers Bangalore
2012-05-10 - club - IPL - male - 548329 - Deccan Chargers vs Delhi Daredevils
2012-05-10 - club - IPL - male - 548361 - Rajasthan Royals vs Chennai Super Kings
2012-05-09 - club - IPL - male - 548360 - Mumbai Indians vs Royal Challengers Bangalore
2012-05-08 - club - IPL - male - 548358 - Pune Warriors vs Rajasthan Royals
2012-05-08 - club - IPL - male - 548359 - Deccan Chargers vs Kings XI Punjab
2012-05-07 - club - IPL - male - 548357 - Delhi Daredevils vs Kolkata Knight Riders
2012-05-06 - club - IPL - male - 548355 - Mumbai Indians vs Chennai Super Kings
2012-05-06 - club - IPL - male - 548356 - Royal Challengers Bangalore vs Deccan Chargers
2012-05-05 - club - IPL - male - 548353 - Kolkata Knight Riders vs Pune Warriors
2012-05-05 - club - IPL - male - 548354 - Kings XI Punjab vs Rajasthan Royals
2012-05-04 - club - IPL - male - 548352 - Chennai Super Kings vs Deccan Chargers
2012-05-03 - club - IPL - male - 548351 - Pune Warriors vs Mumbai Indians
2012-05-02 - club - IPL - male - 548350 - Royal Challengers Bangalore vs Kings XI Punjab
2012-05-01 - club - IPL - male - 548348 - Deccan Chargers vs Pune Warriors
2012-05-01 - club - IPL - male - 548349 - Rajasthan Royals vs Delhi Daredevils
2012-04-30 - club - IPL - male - 548347 - Chennai Super Kings vs Kolkata Knight Riders
2012-04-29 - club - IPL - male - 548345 - Delhi Daredevils vs Rajasthan Royals
2012-04-29 - club - IPL - male - 548346 - Mumbai Indians vs Deccan Chargers
2012-04-28 - club - IPL - male - 548343 - Chennai Super Kings vs Kings XI Punjab
2012-04-28 - club - IPL - male - 548344 - Kolkata Knight Riders vs Royal Challengers Bangalore
2012-04-27 - club - IPL - male - 548342 - Delhi Daredevils vs Mumbai Indians
2012-04-26 - club - IPL - male - 548341 - Pune Warriors vs Deccan Chargers
2012-04-25 - club - IPL - male - 548339 - Kings XI Punjab vs Mumbai Indians
2012-04-24 - club - IPL - male - 548337 - Pune Warriors vs Delhi Daredevils
2012-04-23 - club - IPL - male - 548336 - Rajasthan Royals vs Royal Challengers Bangalore
2012-04-22 - club - IPL - male - 548334 - Mumbai Indians vs Kings XI Punjab
2012-04-22 - club - IPL - male - 548335 - Deccan Chargers vs Kolkata Knight Riders
2012-04-21 - club - IPL - male - 548332 - Chennai Super Kings vs Rajasthan Royals
2012-04-21 - club - IPL - male - 548333 - Delhi Daredevils vs Pune Warriors
2012-04-20 - club - IPL - male - 548331 - Kings XI Punjab vs Royal Challengers Bangalore
2012-04-19 - club - IPL - male - 548321 - Delhi Daredevils vs Deccan Chargers
2012-04-19 - club - IPL - male - 548330 - Chennai Super Kings vs Pune Warriors
2012-04-18 - club - IPL - male - 548328 - Kings XI Punjab vs Kolkata Knight Riders
2012-04-17 - club - IPL - male - 548326 - Rajasthan Royals vs Deccan Chargers
2012-04-17 - club - IPL - male - 548327 - Royal Challengers Bangalore vs Pune Warriors
2012-04-16 - club - IPL - male - 548325 - Mumbai Indians vs Delhi Daredevils
2012-04-15 - club - IPL - male - 548323 - Kolkata Knight Riders vs Kings XI Punjab
2012-04-15 - club - IPL - male - 548324 - Royal Challengers Bangalore vs Rajasthan Royals
2012-04-14 - club - IPL - male - 548322 - Pune Warriors vs Chennai Super Kings
2012-04-13 - club - IPL - male - 548320 - Kolkata Knight Riders vs Rajasthan Royals
2012-04-12 - club - IPL - male - 548318 - Chennai Super Kings vs Royal Challengers Bangalore
2012-04-12 - club - IPL - male - 548319 - Kings XI Punjab vs Pune Warriors
2012-04-11 - club - IPL - male - 548317 - Mumbai Indians vs Rajasthan Royals
2012-04-10 - club - IPL - male - 548315 - Royal Challengers Bangalore vs Kolkata Knight Riders
2012-04-10 - club - IPL - male - 548316 - Delhi Daredevils vs Chennai Super Kings
2012-04-09 - club - IPL - male - 548314 - Deccan Chargers vs Mumbai Indians
2012-04-08 - club - IPL - male - 548312 - Rajasthan Royals vs Kolkata Knight Riders
2012-04-08 - club - IPL - male - 548313 - Pune Warriors vs Kings XI Punjab
2012-04-07 - club - IPL - male - 548310 - Royal Challengers Bangalore vs Delhi Daredevils
2012-04-07 - club - IPL - male - 548311 - Deccan Chargers vs Chennai Super Kings
2012-04-06 - club - IPL - male - 548308 - Mumbai Indians vs Pune Warriors
2012-04-06 - club - IPL - male - 548309 - Rajasthan Royals vs Kings XI Punjab
2012-04-05 - club - IPL - male - 548307 - Kolkata Knight Riders vs Delhi Daredevils
2012-04-04 - club - IPL - male - 548306 - Chennai Super Kings vs Mumbai Indians
2011-05-28 - club - IPL - male - 501271 - Chennai Super Kings vs Royal Challengers Bangalore
2011-05-27 - club - IPL - male - 501270 - Royal Challengers Bangalore vs Mumbai Indians
2011-05-25 - club - IPL - male - 501269 - Mumbai Indians vs Kolkata Knight Riders
2011-05-24 - club - IPL - male - 501268 - Royal Challengers Bangalore vs Chennai Super Kings
2011-05-22 - club - IPL - male - 501266 - Royal Challengers Bangalore vs Chennai Super Kings
2011-05-22 - club - IPL - male - 501267 - Kolkata Knight Riders vs Mumbai Indians
2011-05-21 - club - IPL - male - 501264 - Kings XI Punjab vs Deccan Chargers
2011-05-21 - club - IPL - male - 501265 - Delhi Daredevils vs Pune Warriors
2011-05-20 - club - IPL - male - 501263 - Mumbai Indians vs Rajasthan Royals
2011-05-19 - club - IPL - male - 501262 - Pune Warriors vs Kolkata Knight Riders
2011-05-18 - club - IPL - male - 501261 - Chennai Super Kings vs Kochi Tuskers Kerala
2011-05-17 - club - IPL - male - 501260 - Kings XI Punjab vs Royal Challengers Bangalore
2011-05-16 - club - IPL - male - 501259 - Pune Warriors vs Deccan Chargers
2011-05-15 - club - IPL - male - 501257 - Kings XI Punjab vs Delhi Daredevils
2011-05-15 - club - IPL - male - 501258 - Kochi Tuskers Kerala vs Rajasthan Royals
2011-05-14 - club - IPL - male - 501255 - Royal Challengers Bangalore vs Kolkata Knight Riders
2011-05-14 - club - IPL - male - 501256 - Mumbai Indians vs Deccan Chargers
2011-05-13 - club - IPL - male - 501254 - Kochi Tuskers Kerala vs Kings XI Punjab
2011-05-12 - club - IPL - male - 501253 - Chennai Super Kings vs Delhi Daredevils
2011-05-11 - club - IPL - male - 501252 - Rajasthan Royals vs Royal Challengers Bangalore
2011-05-10 - club - IPL - male - 501250 - Deccan Chargers vs Pune Warriors
2011-05-10 - club - IPL - male - 501251 - Kings XI Punjab vs Mumbai Indians
2011-05-09 - club - IPL - male - 501249 - Rajasthan Royals vs Chennai Super Kings
2011-05-08 - club - IPL - male - 501247 - Royal Challengers Bangalore vs Kochi Tuskers Kerala
2011-05-08 - club - IPL - male - 501248 - Kings XI Punjab vs Pune Warriors
2011-05-07 - club - IPL - male - 501245 - Kolkata Knight Riders vs Chennai Super Kings
2011-05-07 - club - IPL - male - 501246 - Mumbai Indians vs Delhi Daredevils
2011-05-06 - club - IPL - male - 501244 - Royal Challengers Bangalore vs Kings XI Punjab
2011-05-05 - club - IPL - male - 501242 - Kochi Tuskers Kerala vs Kolkata Knight Riders
2011-05-05 - club - IPL - male - 501243 - Deccan Chargers vs Delhi Daredevils
2011-05-04 - club - IPL - male - 501240 - Chennai Super Kings vs Rajasthan Royals
2011-05-04 - club - IPL - male - 501241 - Pune Warriors vs Mumbai Indians
2011-05-03 - club - IPL - male - 501239 - Deccan Chargers vs Kolkata Knight Riders
2011-05-02 - club - IPL - male - 501237 - Mumbai Indians vs Kings XI Punjab
2011-05-02 - club - IPL - male - 501238 - Delhi Daredevils vs Kochi Tuskers Kerala
2011-05-01 - club - IPL - male - 501235 - Rajasthan Royals vs Pune Warriors
2011-05-01 - club - IPL - male - 501236 - Chennai Super Kings vs Deccan Chargers
2011-04-30 - club - IPL - male - 501233 - Kochi Tuskers Kerala vs Delhi Daredevils
2011-04-30 - club - IPL - male - 501234 - Kolkata Knight Riders vs Kings XI Punjab
2011-04-29 - club - IPL - male - 501231 - Rajasthan Royals vs Mumbai Indians
2011-04-29 - club - IPL - male - 501232 - Royal Challengers Bangalore vs Pune Warriors
2011-04-28 - club - IPL - male - 501230 - Delhi Daredevils vs Kolkata Knight Riders
2011-04-27 - club - IPL - male - 501228 - Pune Warriors vs Chennai Super Kings
2011-04-27 - club - IPL - male - 501229 - Kochi Tuskers Kerala vs Deccan Chargers
2011-04-26 - club - IPL - male - 501227 - Delhi Daredevils vs Royal Challengers Bangalore
2011-04-25 - club - IPL - male - 501226 - Chennai Super Kings vs Pune Warriors
2011-04-24 - club - IPL - male - 501224 - Deccan Chargers vs Mumbai Indians
2011-04-24 - club - IPL - male - 501225 - Rajasthan Royals vs Kochi Tuskers Kerala
2011-04-23 - club - IPL - male - 501223 - Delhi Daredevils vs Kings XI Punjab
2011-04-22 - club - IPL - male - 501221 - Mumbai Indians vs Chennai Super Kings
2011-04-22 - club - IPL - male - 501222 - Kolkata Knight Riders vs Royal Challengers Bangalore
2011-04-21 - club - IPL - male - 501220 - Kings XI Punjab vs Rajasthan Royals
2011-04-20 - club - IPL - male - 501218 - Mumbai Indians vs Pune Warriors
2011-04-20 - club - IPL - male - 501219 - Kolkata Knight Riders vs Kochi Tuskers Kerala
2011-04-19 - club - IPL - male - 501216 - Delhi Daredevils vs Deccan Chargers
2011-04-18 - club - IPL - male - 501215 - Kochi Tuskers Kerala vs Chennai Super Kings
2011-04-17 - club - IPL - male - 501213 - Pune Warriors vs Delhi Daredevils
2011-04-17 - club - IPL - male - 501214 - Kolkata Knight Riders vs Rajasthan Royals
2011-04-16 - club - IPL - male - 501211 - Chennai Super Kings vs Royal Challengers Bangalore
2011-04-16 - club - IPL - male - 501212 - Deccan Chargers vs Kings XI Punjab
2011-04-15 - club - IPL - male - 501209 - Rajasthan Royals vs Kolkata Knight Riders
2011-04-15 - club - IPL - male - 501210 - Mumbai Indians vs Kochi Tuskers Kerala
2011-04-14 - club - IPL - male - 501208 - Deccan Chargers vs Royal Challengers Bangalore
2011-04-13 - club - IPL - male - 501206 - Kings XI Punjab vs Chennai Super Kings
2011-04-13 - club - IPL - male - 501207 - Pune Warriors vs Kochi Tuskers Kerala
2011-04-12 - club - IPL - male - 501204 - Rajasthan Royals vs Delhi Daredevils
2011-04-12 - club - IPL - male - 501205 - Royal Challengers Bangalore vs Mumbai Indians
2011-04-11 - club - IPL - male - 501203 - Kolkata Knight Riders vs Deccan Chargers
2011-04-10 - club - IPL - male - 501201 - Delhi Daredevils vs Mumbai Indians
2011-04-10 - club - IPL - male - 501202 - Pune Warriors vs Kings XI Punjab
2011-04-09 - club - IPL - male - 501199 - Deccan Chargers vs Rajasthan Royals
2011-04-09 - club - IPL - male - 501200 - Kochi Tuskers Kerala vs Royal Challengers Bangalore
2011-04-08 - club - IPL - male - 501198 - Chennai Super Kings vs Kolkata Knight Riders
2010-04-25 - club - IPL - male - 419165 - Chennai Super Kings vs Mumbai Indians
2010-04-24 - club - IPL - male - 419164 - Royal Challengers Bangalore vs Deccan Chargers
2010-04-22 - club - IPL - male - 419163 - Chennai Super Kings vs Deccan Chargers
2010-04-21 - club - IPL - male - 419162 - Royal Challengers Bangalore vs Mumbai Indians
2010-04-19 - club - IPL - male - 419161 - Kolkata Knight Riders vs Mumbai Indians
2010-04-18 - club - IPL - male - 419159 - Kings XI Punjab vs Chennai Super Kings
2010-04-18 - club - IPL - male - 419160 - Delhi Daredevils vs Deccan Chargers
2010-04-17 - club - IPL - male - 419157 - Royal Challengers Bangalore vs Mumbai Indians
2010-04-17 - club - IPL - male - 419158 - Kolkata Knight Riders vs Rajasthan Royals
2010-04-16 - club - IPL - male - 419156 - Kings XI Punjab vs Deccan Chargers
2010-04-15 - club - IPL - male - 419155 - Chennai Super Kings vs Delhi Daredevils
2010-04-14 - club - IPL - male - 419154 - Rajasthan Royals vs Royal Challengers Bangalore
2010-04-13 - club - IPL - male - 419152 - Mumbai Indians vs Delhi Daredevils
2010-04-13 - club - IPL - male - 419153 - Chennai Super Kings vs Kolkata Knight Riders
2010-04-12 - club - IPL - male - 419151 - Deccan Chargers vs Royal Challengers Bangalore
2010-04-11 - club - IPL - male - 419149 - Delhi Daredevils vs Kings XI Punjab
2010-04-11 - club - IPL - male - 419150 - Rajasthan Royals vs Mumbai Indians
2010-04-10 - club - IPL - male - 419147 - Deccan Chargers vs Chennai Super Kings
2010-04-10 - club - IPL - male - 419148 - Royal Challengers Bangalore vs Kolkata Knight Riders
2010-04-09 - club - IPL - male - 419146 - Kings XI Punjab vs Mumbai Indians
2010-04-08 - club - IPL - male - 419145 - Royal Challengers Bangalore vs Deccan Chargers
2010-04-07 - club - IPL - male - 419143 - Rajasthan Royals vs Kings XI Punjab
2010-04-07 - club - IPL - male - 419144 - Kolkata Knight Riders vs Delhi Daredevils
2010-04-06 - club - IPL - male - 419142 - Chennai Super Kings vs Mumbai Indians
2010-04-05 - club - IPL - male - 419141 - Deccan Chargers vs Rajasthan Royals
2010-04-04 - club - IPL - male - 419139 - Kolkata Knight Riders vs Kings XI Punjab
2010-04-04 - club - IPL - male - 419140 - Delhi Daredevils vs Royal Challengers Bangalore
2010-04-03 - club - IPL - male - 419137 - Chennai Super Kings vs Rajasthan Royals
2010-04-03 - club - IPL - male - 419138 - Mumbai Indians vs Deccan Chargers
2010-04-02 - club - IPL - male - 419136 - Kings XI Punjab vs Royal Challengers Bangalore
2010-04-01 - club - IPL - male - 419135 - Kolkata Knight Riders vs Deccan Chargers
2010-03-31 - club - IPL - male - 419133 - Chennai Super Kings vs Royal Challengers Bangalore
2010-03-31 - club - IPL - male - 419134 - Delhi Daredevils vs Rajasthan Royals
2010-03-30 - club - IPL - male - 419132 - Mumbai Indians vs Kings XI Punjab
2010-03-29 - club - IPL - male - 419131 - Delhi Daredevils vs Kolkata Knight Riders
2010-03-28 - club - IPL - male - 419129 - Rajasthan Royals vs Chennai Super Kings
2010-03-28 - club - IPL - male - 419130 - Deccan Chargers vs Mumbai Indians
2010-03-27 - club - IPL - male - 419127 - Kings XI Punjab vs Kolkata Knight Riders
2010-03-26 - club - IPL - male - 419126 - Rajasthan Royals vs Deccan Chargers
2010-03-25 - club - IPL - male - 419125 - Mumbai Indians vs Chennai Super Kings
2010-03-25 - club - IPL - male - 419128 - Royal Challengers Bangalore vs Delhi Daredevils
2010-03-24 - club - IPL - male - 419124 - Kings XI Punjab vs Rajasthan Royals
2010-03-23 - club - IPL - male - 419123 - Royal Challengers Bangalore vs Chennai Super Kings
2010-03-22 - club - IPL - male - 419122 - Mumbai Indians vs Kolkata Knight Riders
2010-03-21 - club - IPL - male - 419120 - Deccan Chargers vs Delhi Daredevils
2010-03-21 - club - IPL - male - 419121 - Chennai Super Kings vs Kings XI Punjab
2010-03-20 - club - IPL - male - 419118 - Rajasthan Royals vs Kolkata Knight Riders
2010-03-20 - club - IPL - male - 419119 - Mumbai Indians vs Royal Challengers Bangalore
2010-03-19 - club - IPL - male - 419116 - Delhi Daredevils vs Chennai Super Kings
2010-03-19 - club - IPL - male - 419117 - Deccan Chargers vs Kings XI Punjab
2010-03-18 - club - IPL - male - 419115 - Royal Challengers Bangalore vs Rajasthan Royals
2010-03-17 - club - IPL - male - 419114 - Delhi Daredevils vs Mumbai Indians
2010-03-16 - club - IPL - male - 419112 - Royal Challengers Bangalore vs Kings XI Punjab
2010-03-16 - club - IPL - male - 419113 - Kolkata Knight Riders vs Chennai Super Kings
2010-03-15 - club - IPL - male - 419111 - Rajasthan Royals vs Delhi Daredevils
2010-03-14 - club - IPL - male - 419109 - Kolkata Knight Riders vs Royal Challengers Bangalore
2010-03-14 - club - IPL - male - 419110 - Chennai Super Kings vs Deccan Chargers
2010-03-13 - club - IPL - male - 419107 - Mumbai Indians vs Rajasthan Royals
2010-03-13 - club - IPL - male - 419108 - Kings XI Punjab vs Delhi Daredevils
2010-03-12 - club - IPL - male - 419106 - Deccan Chargers vs Kolkata Knight Riders
2009-05-24 - club - IPL - male - 392239 - Royal Challengers Bangalore vs Deccan Chargers
2009-05-23 - club - IPL - male - 392238 - Royal Challengers Bangalore vs Chennai Super Kings
2009-05-22 - club - IPL - male - 392237 - Delhi Daredevils vs Deccan Chargers
2009-05-21 - club - IPL - male - 392235 - Delhi Daredevils vs Mumbai Indians
2009-05-21 - club - IPL - male - 392236 - Royal Challengers Bangalore vs Deccan Chargers
2009-05-20 - club - IPL - male - 392233 - Kolkata Knight Riders vs Rajasthan Royals
2009-05-20 - club - IPL - male - 392234 - Chennai Super Kings vs Kings XI Punjab
2009-05-19 - club - IPL - male - 392232 - Royal Challengers Bangalore vs Delhi Daredevils
2009-05-18 - club - IPL - male - 392231 - Chennai Super Kings vs Kolkata Knight Riders
2009-05-17 - club - IPL - male - 392229 - Deccan Chargers vs Kings XI Punjab
2009-05-17 - club - IPL - male - 392230 - Delhi Daredevils vs Rajasthan Royals
2009-05-16 - club - IPL - male - 392227 - Chennai Super Kings vs Mumbai Indians
2009-05-16 - club - IPL - male - 392228 - Deccan Chargers vs Kolkata Knight Riders
2009-05-15 - club - IPL - male - 392226 - Delhi Daredevils vs Kings XI Punjab
2009-05-14 - club - IPL - male - 392224 - Royal Challengers Bangalore vs Chennai Super Kings
2009-05-14 - club - IPL - male - 392225 - Mumbai Indians vs Rajasthan Royals
2009-05-13 - club - IPL - male - 392223 - Deccan Chargers vs Delhi Daredevils
2009-05-12 - club - IPL - male - 392221 - Royal Challengers Bangalore vs Kolkata Knight Riders
2009-05-12 - club - IPL - male - 392222 - Kings XI Punjab vs Mumbai Indians
2009-05-11 - club - IPL - male - 392220 - Deccan Chargers vs Rajasthan Royals
2009-05-10 - club - IPL - male - 392218 - Royal Challengers Bangalore vs Mumbai Indians
2009-05-10 - club - IPL - male - 392219 - Delhi Daredevils vs Kolkata Knight Riders
2009-05-09 - club - IPL - male - 392216 - Deccan Chargers vs Kings XI Punjab
2009-05-09 - club - IPL - male - 392217 - Chennai Super Kings vs Rajasthan Royals
2009-05-08 - club - IPL - male - 392215 - Delhi Daredevils vs Mumbai Indians
2009-05-07 - club - IPL - male - 392213 - Royal Challengers Bangalore vs Rajasthan Royals
2009-05-07 - club - IPL - male - 392214 - Chennai Super Kings vs Kings XI Punjab
2009-05-06 - club - IPL - male - 392212 - Deccan Chargers vs Mumbai Indians
2009-05-05 - club - IPL - male - 392210 - Kings XI Punjab vs Rajasthan Royals
2009-05-05 - club - IPL - male - 392211 - Delhi Daredevils vs Kolkata Knight Riders
2009-05-04 - club - IPL - male - 392209 - Chennai Super Kings vs Deccan Chargers
2009-05-03 - club - IPL - male - 392207 - Kings XI Punjab vs Kolkata Knight Riders
2009-05-03 - club - IPL - male - 392208 - Royal Challengers Bangalore vs Mumbai Indians
2009-05-02 - club - IPL - male - 392205 - Deccan Chargers vs Rajasthan Royals
2009-05-02 - club - IPL - male - 392206 - Chennai Super Kings vs Delhi Daredevils
2009-05-01 - club - IPL - male - 392203 - Kolkata Knight Riders vs Mumbai Indians
2009-05-01 - club - IPL - male - 392204 - Royal Challengers Bangalore vs Kings XI Punjab
2009-04-30 - club - IPL - male - 392201 - Deccan Chargers vs Delhi Daredevils
2009-04-30 - club - IPL - male - 392202 - Chennai Super Kings vs Rajasthan Royals
2009-04-29 - club - IPL - male - 392199 - Royal Challengers Bangalore vs Kolkata Knight Riders
2009-04-29 - club - IPL - male - 392200 - Kings XI Punjab vs Mumbai Indians
2009-04-28 - club - IPL - male - 392198 - Delhi Daredevils vs Rajasthan Royals
2009-04-27 - club - IPL - male - 392196 - Chennai Super Kings vs Deccan Chargers
2009-04-27 - club - IPL - male - 392197 - Kolkata Knight Riders vs Mumbai Indians
2009-04-26 - club - IPL - male - 392194 - Royal Challengers Bangalore vs Delhi Daredevils
2009-04-26 - club - IPL - male - 392195 - Kings XI Punjab vs Rajasthan Royals
2009-04-25 - club - IPL - male - 392192 - Deccan Chargers vs Mumbai Indians
2009-04-24 - club - IPL - male - 392191 - Royal Challengers Bangalore vs Kings XI Punjab
2009-04-23 - club - IPL - male - 392189 - Chennai Super Kings vs Delhi Daredevils
2009-04-23 - club - IPL - male - 392190 - Kolkata Knight Riders vs Rajasthan Royals
2009-04-22 - club - IPL - male - 392188 - Royal Challengers Bangalore vs Deccan Chargers
2009-04-21 - club - IPL - male - 392186 - Kings XI Punjab vs Kolkata Knight Riders
2009-04-20 - club - IPL - male - 392185 - Royal Challengers Bangalore vs Chennai Super Kings
2009-04-19 - club - IPL - male - 392183 - Delhi Daredevils vs Kings XI Punjab
2009-04-19 - club - IPL - male - 392184 - Deccan Chargers vs Kolkata Knight Riders
2009-04-18 - club - IPL - male - 392181 - Chennai Super Kings vs Mumbai Indians
2009-04-18 - club - IPL - male - 392182 - Royal Challengers Bangalore vs Rajasthan Royals
2008-06-01 - club - IPL - male - 336040 - Chennai Super Kings vs Rajasthan Royals
2008-05-31 - club - IPL - male - 336039 - Chennai Super Kings vs Kings XI Punjab
2008-05-30 - club - IPL - male - 336038 - Delhi Daredevils vs Rajasthan Royals
2008-05-28 - club - IPL - male - 336012 - Royal Challengers Bangalore vs Mumbai Indians
2008-05-28 - club - IPL - male - 336019 - Kings XI Punjab vs Rajasthan Royals
2008-05-27 - club - IPL - male - 336037 - Deccan Chargers vs Chennai Super Kings
2008-05-26 - club - IPL - male - 336036 - Rajasthan Royals vs Mumbai Indians
2008-05-25 - club - IPL - male - 336002 - Deccan Chargers vs Royal Challengers Bangalore
2008-05-25 - club - IPL - male - 336035 - Kolkata Knight Riders vs Kings XI Punjab
2008-05-24 - club - IPL - male - 336032 - Delhi Daredevils vs Mumbai Indians
2008-05-24 - club - IPL - male - 336033 - Chennai Super Kings vs Rajasthan Royals
2008-05-23 - club - IPL - male - 336031 - Kings XI Punjab vs Deccan Chargers
2008-05-21 - club - IPL - male - 336028 - Mumbai Indians vs Kings XI Punjab
2008-05-21 - club - IPL - male - 336029 - Chennai Super Kings vs Royal Challengers Bangalore
2008-05-20 - club - IPL - male - 336027 - Kolkata Knight Riders vs Rajasthan Royals
2008-05-19 - club - IPL - male - 336026 - Royal Challengers Bangalore vs Delhi Daredevils
2008-05-18 - club - IPL - male - 336024 - Deccan Chargers vs Mumbai Indians
2008-05-18 - club - IPL - male - 336025 - Kolkata Knight Riders vs Chennai Super Kings
2008-05-17 - club - IPL - male - 336022 - Delhi Daredevils vs Kings XI Punjab
2008-05-17 - club - IPL - male - 336023 - Rajasthan Royals vs Royal Challengers Bangalore
2008-05-16 - club - IPL - male - 336021 - Mumbai Indians vs Kolkata Knight Riders
2008-05-15 - club - IPL - male - 336020 - Delhi Daredevils vs Deccan Chargers
2008-05-14 - club - IPL - male - 336018 - Mumbai Indians vs Chennai Super Kings
2008-05-13 - club - IPL - male - 336017 - Kolkata Knight Riders vs Delhi Daredevils
2008-05-12 - club - IPL - male - 336016 - Kings XI Punjab vs Royal Challengers Bangalore
2008-05-11 - club - IPL - male - 336014 - Deccan Chargers vs Kolkata Knight Riders
2008-05-11 - club - IPL - male - 336015 - Rajasthan Royals vs Delhi Daredevils
2008-05-10 - club - IPL - male - 336013 - Chennai Super Kings vs Kings XI Punjab
2008-05-09 - club - IPL - male - 336011 - Rajasthan Royals vs Deccan Chargers
2008-05-08 - club - IPL - male - 336009 - Delhi Daredevils vs Chennai Super Kings
2008-05-08 - club - IPL - male - 336010 - Kolkata Knight Riders vs Royal Challengers Bangalore
2008-05-07 - club - IPL - male - 336008 - Mumbai Indians vs Rajasthan Royals
2008-05-06 - club - IPL - male - 336007 - Chennai Super Kings vs Deccan Chargers
2008-05-05 - club - IPL - male - 336006 - Royal Challengers Bangalore vs Kings XI Punjab
2008-05-04 - club - IPL - male - 336004 - Mumbai Indians vs Delhi Daredevils
2008-05-04 - club - IPL - male - 336005 - Rajasthan Royals vs Chennai Super Kings
2008-05-03 - club - IPL - male - 336003 - Kings XI Punjab vs Kolkata Knight Riders
2008-05-03 - club - IPL - male - 336034 - Royal Challengers Bangalore vs Deccan Chargers
2008-05-02 - club - IPL - male - 336001 - Chennai Super Kings vs Delhi Daredevils
2008-05-01 - club - IPL - male - 335999 - Deccan Chargers vs Kings XI Punjab
2008-05-01 - club - IPL - male - 336000 - Rajasthan Royals vs Kolkata Knight Riders
2008-04-30 - club - IPL - male - 335998 - Delhi Daredevils vs Royal Challengers Bangalore
2008-04-29 - club - IPL - male - 335997 - Kolkata Knight Riders vs Mumbai Indians
2008-04-28 - club - IPL - male - 335996 - Royal Challengers Bangalore vs Chennai Super Kings
2008-04-27 - club - IPL - male - 335994 - Mumbai Indians vs Deccan Chargers
2008-04-27 - club - IPL - male - 335995 - Kings XI Punjab vs Delhi Daredevils
2008-04-26 - club - IPL - male - 335992 - Royal Challengers Bangalore vs Rajasthan Royals
2008-04-26 - club - IPL - male - 335993 - Chennai Super Kings vs Kolkata Knight Riders
2008-04-25 - club - IPL - male - 335991 - Kings XI Punjab vs Mumbai Indians
2008-04-24 - club - IPL - male - 335990 - Deccan Chargers vs Rajasthan Royals
2008-04-23 - club - IPL - male - 335989 - Chennai Super Kings vs Mumbai Indians
2008-04-22 - club - IPL - male - 335988 - Deccan Chargers vs Delhi Daredevils
2008-04-21 - club - IPL - male - 335987 - Rajasthan Royals vs Kings XI Punjab
2008-04-20 - club - IPL - male - 335985 - Mumbai Indians vs Royal Challengers Bangalore
2008-04-20 - club - IPL - male - 335986 - Kolkata Knight Riders vs Deccan Chargers
2008-04-19 - club - IPL - male - 335983 - Kings XI Punjab vs Chennai Super Kings
2008-04-19 - club - IPL - male - 335984 - Delhi Daredevils vs Rajasthan Royals
2008-04-18 - club - IPL - male - 335982 - Royal Challengers Bangalore vs Kolkata Knight Riders

Consolidated data
-----------------

You may notice that there is an extra CSV file in this archive, called
"all_matches.csv". This file, as the name suggests, contains all of the
matches from the archive in a single CSV. Hopefully it will make use of
the data easier in some cases.

Further information
-------------------

You can find all of our currently available data at https://cricsheet.org/

You can contact me via the following methods:
  Email  : stephen@cricsheet.org
  Twitter: @cricsheet
