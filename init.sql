COPY city (city_id, city_name, city_coordinates, city_population) FROM stdin;
1	Istanbul	41.0082376,28.9783589	11111
3	Brussels	50.8503396,4.3517103	31
5	Trabzon	41.0026969,39.7167633	6161
6	Moscow	55.755826,37.6173	1231
7	Ankara	39.9333635,32.8597419	7000
8	Paris	48.856614,2.3522219	1234
9	St. Petersburg	27.7518284,-82.6267345	5555
10	Kayseri	38.720489,35.48259700000001	5556
11	London	51.5073509,-0.1277583	6661
12	Rome	41.9027835,12.4963655	4567
13	Rize	41.025511,40.517666	100000
14	Abu Dhabi	24.2991738,54.6972774	5555
15	Baku	40.40926169999999,49.8670924	1111
16	Baghdad	33.3128057,44.3614875	1111
17	Bratislava	48.1458923,17.1071373	1111
18	Belgrade	44.786568,20.4489216	1111
19	Tilatte	43.242991,-0.487055	666
21	Mordor	33.1763714,-96.78859899999999	50000
\.

COPY country (country_id, country_name, country_population, capital) FROM stdin;
7	Turkey	1111	7
8	France	456	8
9	Russia	5555	6
10	England	555	11
11	Italy	6789	12
12	Serbia	1111	18
13	Slovakia	4444	17
14	UAE	5555	14
15	Azerbaijan	4567	15
16	Iraq	11111	16
17	Tilatteleroğlu	9752	19
\.

COPY league (league_id, league_name, league_country, league_start_date) FROM stdin;
3	Süper Toto	7	1969-01-01
4	Ruski Comrade	9	1955-05-05
5	Rezzo Italiano	11	1965-05-06
6	Le League	8	1977-05-12
7	Elizabeth Premier	10	1967-12-01
\.

COPY log (log_id, log_description, log_author, log_time) FROM stdin;
1	Added Romania to Countries	1	2015-12-12
2	Added Istanbul to Cities	1	2015-12-12
3	Added Istanbul to Cities	1	2015-12-12
4	Added Citizen to Person Types	1	2015-12-12
5	Added Hakan Balta to Persons	1	2015-12-12
6	Added Colorado to Cities	1	2015-12-12
7	Added Red Card to Penalty Types	1	2015-12-12
8	Added penalty for1 to Penalties	1	2015-12-12
9	Added Bundesliga to Leagues	1	2015-12-12
10	Added Coach to Person Types	1	2015-12-12
11	Added Couch to Person Types	1	2015-12-12
12	Added Abe to Persons	1	2015-12-12
13	Added Ace to Persons	1	2015-12-12
14	Added Leopeard to Teams	1	2015-12-12
15	Added Bunda to Players	1	2015-12-12
16	Added penalty forHakan Balta to Penalties	1	2015-12-12
17	Added penalty forHakan Balta to Penalties	1	2015-12-12
18	Added Baltimore to Cities	1	2015-12-12
19	Added penalty forHakan Balta to Penalties	1	2015-12-12
20	Added Yellow to Penalty Types	1	2015-12-12
21	Added penalty forHakan Balta to Penalties	1	2015-12-12
22	Added Old traford to Stadiums	1	2015-12-12
23	Added KALe to Sponsorships	1	2015-12-12
24	Added penalty forHakan Balta to Penalties	1	2015-12-12
25	Deleted Ace from Persons	1	2015-12-12
26	Updated element with id=6 in Penalties	1	2015-12-12
27	Updated element with id=3 in Cities	1	2015-12-12
28	Added Trabzon to Cities	1	2015-12-12
29	Added Hawks to Teams	1	2015-12-12
30	Updated element with id=1 in Teams	1	2015-12-12
31	Deleted Leopeard2 from Teams	1	2015-12-12
32	Added Karpuz to Players	1	2015-12-12
33	Added Old Traford to Stadiums	1	2015-12-12
34	Added Crows to Teams	1	2015-12-12
35	Added match between Crowsand Hawks to Matches	1	2015-12-12
36	Deleted Romania from Countries	1	2015-12-12
37	Deleted Old Traford from Stadiums	1	2015-12-12
38	Added Bernabeu to Stadiums	1	2015-12-12
39	Deleted Match Between Crows and Hawks from Matches	1	2015-12-12
40	Added Penalty For Hakan Balta to Penalties	1	2015-12-12
41	Added Penalty For Hakan Balta to Penalties	1	2015-12-12
42	Added Ali Baba to Persons	1	2015-12-12
43	Deleted Hakan Balta from Persons	1	2015-12-12
44	Updated Element With id=4 in Persons	1	2015-12-12
45	Added Kiev to Cities	1	2015-12-12
46	Deleted Baltimore from Cities	1	2015-12-12
47	Updated Element With id=6 in Cities	1	2015-12-12
48	Added Match Between Crows and Hawks to Matches	1	2015-12-12
49	Deleted Match Between Crows and Hawks from Matches	1	2015-12-12
50	Added Match Between Crows and Hawks to Matches	1	2015-12-12
51	Deleted Match Between Crows and Hawks from Matches	1	2015-12-12
52	Added Match Between Crows and Hawks to Matches	1	2015-12-12
53	Updated Element With id=4 in Matches	1	2015-12-12
54	Added Maret Sucuk to Sponsorships	1	2015-12-12
55	Added Penalty For Abe to Penalties	1	2015-12-12
56	Added Penalty For Abe to Penalties	1	2015-12-12
57	Added Penalty For Abe to Penalties	1	2015-12-12
58	Added Garpuz to Players	1	2015-12-12
59	Added Garpuz to Players	1	2015-12-12
60	Deleted Garpuz from Players	1	2015-12-12
61	Updated Element With id=2 in Teams	1	2015-12-12
62	Updated Element With id=2 in Teams	1	2015-12-12
63	Deleted Hawks2 from Teams	1	2015-12-12
64	Added Pattis to Teams	1	2015-12-12
65	Deleted Penalty For Abe from Penalties	1	2015-12-12
66	Added Player1 to Players	1	2015-12-12
67	Added Player1 to Players	1	2015-12-12
68	Added Player1 to Players	1	2015-12-12
69	Added Player1 to Players	1	2015-12-12
70	Added Player1 to Players	1	2015-12-12
71	Added Player1 to Players	1	2015-12-12
72	Added Player1 to Players	1	2015-12-12
73	Added Player1 to Players	1	2015-12-12
74	Added Player1 to Players	1	2015-12-12
75	Deleted Player1 from Players	1	2015-12-12
76	Deleted Player1 from Players	1	2015-12-12
77	Deleted Player1 from Players	1	2015-12-12
78	Deleted Player1 from Players	1	2015-12-12
79	Deleted Player1 from Players	1	2015-12-12
80	Deleted Player1 from Players	1	2015-12-12
81	Deleted Player1 from Players	1	2015-12-12
82	Deleted Player1 from Players	1	2015-12-12
83	Updated Element With id=3 in Teams	1	2015-12-12
84	Added Pattisland to Countries	1	2015-12-12
85	Added Fukrania to Countries	1	2015-12-12
86	Updated Element With id=3 in Countries	1	2015-12-12
87	Added Ananza to Countries	1	2015-12-12
88	Deleted Pattisland2 from Countries	1	2015-12-12
89	Updated Element With id=4 in Countries	1	2015-12-12
90	Added Turkey to Countries	1	2015-12-12
91	Added Bundesliga to Leagues	1	2015-12-12
92	Added Old Traford to Stadiums	1	2015-12-12
93	Added Match Between Crowss and Pattis to Matches	1	2015-12-12
94	Updated Element With id=1 in Matches	1	2015-12-12
95	Deleted Match Between Pattis and Pattis from Matches	1	2015-12-12
96	Added Grand Tournament to Tournaments	1	2015-12-13
97	Added Medium Tournament to Tournaments	1	2015-12-13
98	Deleted Medium Tournament from Tournaments	1	2015-12-13
99	Updated Element With id=2 in Leagues	1	2015-12-13
100	Updated Element With id=2 in Leagues	1	2015-12-13
101	Updated Element With id=1 in Tournaments	1	2015-12-13
102	Added Match Between Crowss and Pattis to Matches	1	2015-12-13
103	Added 123 to Teams	1	2015-12-13
104	Added Match Between 123 and Crowss to Matches	1	2015-12-13
105	Added Popularity Info for 4 to Popularity	1	2015-12-13
106	Added Popularity Info for 4 to Popularity	1	2015-12-13
107	Added Popularity Info for 4 to Popularity	1	2015-12-13
108	Added Popularity Info for 4 to Popularity	1	2015-12-13
109	Added Popularity Info for 4 to Popularity	1	2015-12-13
110	Deleted Crowss from Teams	1	2015-12-13
111	Added Match Between Pattis and Pattis to Matches	1	2015-12-13
112	Added Popularity Info for 4 to Popularity	1	2015-12-13
113	Deleted Popularity Info For Pattis from Penalties	1	2015-12-13
114	Added Popularity Info for 4 to Popularity	1	2015-12-13
115	Deleted Popularity Info For Pattis from Penalties	1	2015-12-13
116	Added Match Between Pattis and 123 to Matches	1	2015-12-13
117	Added Popularity Info for 4 to Popularity	1	2015-12-13
118	Added Popularity Info for 4 to Popularity	1	2015-12-13
119	Added Popularity Info for 4 to Popularity	1	2015-12-13
120	Deleted Popularity Info For Pattis from Penalties	1	2015-12-13
121	Added Match Between 123 and Pattis to Matches	2	2015-12-13
122	Deleted Abe from Persons	2	2015-12-13
123	Deleted Ali Baban from Persons	2	2015-12-13
124	Deleted Fukrania from Countries	2	2015-12-13
125	Deleted Ananza from Countries	2	2015-12-13
126	Deleted Turkey from Countries	2	2015-12-13
127	Added Dictator to Person Types	2	2015-12-13
128	Added Pimp to Person Types	2	2015-12-13
129	Added Dude to Person Types	2	2015-12-13
130	Added Onichan to Person Types	2	2015-12-13
131	Added Mayor to Person Types	2	2015-12-13
132	Added Criminal to Person Types	2	2015-12-13
133	Added Ninja to Person Types	2	2015-12-13
134	Added Normal Citizen to Person Types	2	2015-12-13
135	Added Yakuza to Person Types	2	2015-12-13
136	Added Selami Yediok to Persons	2	2015-12-13
137	Added Ankara to Cities	2	2015-12-13
138	Added Paris to Cities	2	2015-12-13
139	Added St. Petersburg to Cities	2	2015-12-13
140	Added Kayseri to Cities	2	2015-12-13
141	Added London to Cities	2	2015-12-13
142	Added Rome to Cities	2	2015-12-13
143	Added Lord Mammoth to Persons	2	2015-12-13
144	Added Selin Ayrancı to Persons	2	2015-12-13
145	Added Yahya Selamlı to Persons	2	2015-12-13
146	Added Bruce Fellow to Persons	2	2015-12-13
147	Added Mahmut Öteberi to Persons	2	2015-12-13
148	Added Haydar Baş to Persons	2	2015-12-13
149	Added Turkey to Countries	2	2015-12-13
150	Added France to Countries	2	2015-12-13
151	Added Russia to Countries	2	2015-12-13
152	Added England to Countries	2	2015-12-13
153	Added Italy to Countries	2	2015-12-13
154	Added Süper Toto to Leagues	2	2015-12-13
155	Added Ruski Comrade to Leagues	2	2015-12-13
156	Added Rezzo Italiano to Leagues	2	2015-12-13
157	Added Le League to Leagues	2	2015-12-13
158	Added Elizabeth Premier to Leagues	2	2015-12-13
159	Added Vladimir Putin to Persons	2	2015-12-13
160	Added Comrade Putin to Teams	2	2015-12-13
161	Added Haydar Yangelir to Persons	2	2015-12-13
162	Added Metin Yazçiz to Persons	2	2015-12-13
163	Added Stephen Olo to Persons	2	2015-12-13
164	Added Queen Elizabeth to Persons	2	2015-12-13
165	Added All Elizabeth to Teams	2	2015-12-13
166	Added France Le Baseball to Teams	2	2015-12-13
167	Added Kayserigücü to Teams	2	2015-12-13
168	Added Ninjas to Teams	2	2015-12-13
169	Added Cool Bros to Teams	2	2015-12-13
170	Added Sexy Stylez to Teams	2	2015-12-13
171	Added Le Le Le to Teams	2	2015-12-13
172	Added Cyka to Teams	2	2015-12-13
173	Added Russian Nuke to Teams	2	2015-12-13
174	Added ISIS Paris to Teams	2	2015-12-13
175	Added Pastırmaspor to Teams	2	2015-12-13
176	Added Tren Gelir Yan Gelir to Teams	2	2015-12-13
177	Added Ruski Supreme to Stadiums	2	2015-12-13
178	Added Elizabethenia to Stadiums	2	2015-12-13
179	Added ISIS Arena to Stadiums	2	2015-12-13
180	Added Pastırma Arena to Stadiums	2	2015-12-13
181	Added Yakuza Arena to Stadiums	2	2015-12-13
182	Added Old Traford to Stadiums	2	2015-12-13
183	Added Baby Arena to Stadiums	2	2015-12-13
184	Added Le Stadia to Stadiums	2	2015-12-13
185	Added Match Between Comrade Putin and All Elizabeth to Matches	2	2015-12-13
186	Added Match Between Comrade Putin and France Le Baseball to Matches	2	2015-12-13
187	Added Match Between All Elizabeth and France Le Baseball to Matches	2	2015-12-13
188	Added Match Between Kayserigücü and Pastırmaspor to Matches	5	2015-12-13
189	Added The Grand Tournament to Tournaments	5	2015-12-13
190	Added Russian Warfare to Tournaments	5	2015-12-13
191	Added Putinspor to Teams	5	2015-12-13
192	Added Rize to Cities	5	2015-12-13
193	Added Recep Tayyip Erdoğan to Persons	5	2015-12-13
194	Added Erdoğanspor to Teams	5	2015-12-13
195	Added Match Between Putinspor and Erdoğanspor to Matches	5	2015-12-13
196	Added Trabzonspor to Teams	5	2015-12-13
197	Added Fenerbahçe to Teams	5	2015-12-13
198	Added Abu Dhabi to Cities	2	2015-12-13
199	Added Match Between Trabzonspor and Fenerbahçe to Matches	5	2015-12-13
200	Added Baku to Cities	2	2015-12-13
201	Added Baghdad to Cities	2	2015-12-13
202	Added Bratislava to Cities	2	2015-12-13
203	Added Belgrade to Cities	2	2015-12-13
204	Added Serbia to Countries	2	2015-12-13
205	Added Slovakia to Countries	2	2015-12-13
206	Added UAE to Countries	2	2015-12-13
207	Added Azerbaijan to Countries	2	2015-12-13
208	Added Iraq to Countries	2	2015-12-13
209	Added Match Between Cyka and Ninjas to Matches	5	2015-12-13
210	Added Russian Soldier 1 to Players	5	2015-12-13
211	Added Russian Soldier 2 to Players	5	2015-12-13
212	Added Russian Soldier 3 to Players	5	2015-12-13
213	Added Russian Commander 1 to Players	5	2015-12-13
214	Added Russian Commander 2 to Players	5	2015-12-13
215	Added Mert Şeker to Persons	5	2015-12-13
216	Added Şekerspor to Teams	5	2015-12-13
217	Added Fukran Akgün to Players	5	2015-12-13
218	Added Umut Yar Özcan to Players	5	2015-12-13
219	Added Oğuz Terem Kural to Players	5	2015-12-13
220	Added Mert Şeker to Players	5	2015-12-13
221	Added Match Between Putinspor and Şekerspor to Matches	5	2015-12-13
222	Added Popularity Info for 6 to Popularity	1	2015-12-13
223	Added Comrade Putin to Team_stats	1	2015-12-13
224	Added Penalty For Selami Yediok to Penalties	1	2015-12-13
225	Added Maret Sucuk to Sponsorships	1	2015-12-13
226	Added şuhutspor to Teams	1	2015-12-13
227	Added fakir to Person Types	1	2015-12-13
228	Added Tilatte to Cities	1	2015-12-13
229	Added Tilattespor to Teams	1	2015-12-13
230	Added Tilattespor to Team_stats	1	2015-12-13
231	Added Tilattiovic to Players	1	2015-12-13
232	Added Tİlattilaler to Sponsorships	1	2015-12-13
233	Added Stadium Tilatte Arena De Manuela to Stadiums	1	2015-12-13
234	Added Tilatteleroğlu to Countries	1	2015-12-13
235	Added Match Between Tilattespor and Ninjas to Matches	1	2015-12-13
236	Added Match Between Tilattespor and Ninjas to Matches	1	2015-12-13
237	Added DROP TABLE Tournaments to Tournaments	1	2015-12-13
238	Deleted DROP TABLE Tournaments from Tournaments	1	2015-12-13
239	Added DROP TABLE People; to Persons	1	2015-12-13
240	Deleted DROP TABLE People; from Persons	1	2015-12-13
241	Added AA;Drop Table Teams to Teams	1	2015-12-13
242	Deleted AA;Drop Table Teams from Teams	1	2015-12-13
243	Added OR 1 = 1 to Persons	1	2015-12-13
244	Deleted OR 1 = 1 from Persons	1	2015-12-13
245	Added 123;DELETE FROM players to Players	1	2015-12-13
246	Deleted 123;DELETE FROM players from Players	1	2015-12-13
247	Added Hobbit to Person Types	1	2015-12-13
248	Added Bilbo Baggins to Persons	1	2015-12-13
249	Added Mordor to Cities	1	2015-12-13
250	Updated Element With id=6 in Persons	1	2015-12-13
251	Added Westboro Baptist Church to Sponsorships	1	2015-12-13
252	Added Westeros Grand Tournament to Tournaments	1	2015-12-13
253	Added Popularity Info for 17 to Popularity	1	2015-12-13
\.

COPY matches (match_id, match_team_1, match_team_2, match_league, match_stadium, match_referee, match_date, match_team1_score, match_team2_score) FROM stdin;
7	6	7	4	7	6	2014-01-01	1	2
8	6	8	4	12	7	2014-06-01	2	3
9	7	8	7	6	11	1111-01-02	4	1
10	9	17	6	8	12	2015-12-12	2	4
11	19	20	6	7	6	2015-11-11	10	20
12	21	22	7	12	17	1995-03-13	2	9
13	14	10	7	6	7	1995-06-06	5	5
14	19	23	3	10	9	2015-09-10	9	24
15	25	10	3	13	14	2015-02-24	21	12
16	25	10	3	13	14	2015-02-24	21	12
\.

COPY penalty (penalty_id, penalty_type, penalty_given_person, penalty_given_date) FROM stdin;
17	1	5	2015-10-11
\.

COPY penalty_type (id, penalty_type_name) FROM stdin;
1	Red Card
2	Yellow
\.

COPY person (person_id, person_name, person_birth_date, person_birth_location, person_type) FROM stdin;
5	Selami Yediok	2985-02-01	1	11
7	Selin Ayrancı	1996-05-01	7	11
8	Yahya Selamlı	1972-06-11	8	5
9	Bruce Fellow	1982-05-01	11	9
10	Mahmut Öteberi	1967-07-02	10	11
11	Haydar Baş	1971-01-05	7	6
12	Vladimir Putin	0121-12-23	6	3
13	Haydar Yangelir	1955-12-31	1	3
14	Metin Yazçiz	1977-01-02	10	3
15	Stephen Olo	1956-01-02	8	3
16	Queen Elizabeth	1901-01-01	11	3
17	Recep Tayyip Erdoğan	1960-10-10	13	3
18	Mert Şeker	1995-03-13	1	3
21	Bilbo Baggins	1398-01-01	13	14
6	Lord Mammoth	1993-05-12	6	8
\.

COPY person_types (id, person_type_name) FROM stdin;
1	Citizen
2	Coach
3	Couch
4	Dictator
5	Pimp
6	Dude
7	Onichan
8	Mayor
9	Criminal
10	Ninja
11	Normal Citizen
12	Yakuza
13	fakir
14	Hobbit
\.

COPY player (player_id, player_name, player_team, player_goals) FROM stdin;
14	Russian Soldier 1	19	5
15	Russian Soldier 2	19	8
16	Russian Soldier 3	19	4
17	Russian Commander 1	19	18
18	Russian Commander 2	19	24
19	Fukran Akgün	23	14
20	Umut Yar Özcan	23	6
21	Oğuz Terem Kural	23	2
22	Mert Şeker	23	1584
23	Tilattiovic	25	31
\.

COPY popularity (popularity_id, team_name, most_popular_match, most_popular_player, supporters) FROM stdin;
11	6	7	12	2000000
12	17	10	21	100000000
\.

COPY sponsorship (sponsorship_id, sponsorship_name, sponsorship_start_date, sponsorship_league, sponsorship_team, sponsorship_person) FROM stdin;
3	Maret Sucuk	2111-01-01	5	7	8
4	Tİlattilaler	1985-02-25	4	25	5
5	Westboro Baptist Church	1995-04-12	3	16	17
\.

COPY stadium (stadium_id, stadium_name, stadium_team, stadium_location, stadium_capacity) FROM stdin;
5	Ruski Supreme	6	6	1231
6	Elizabethenia	7	11	1111
7	ISIS Arena	8	8	7777
8	Pastırma Arena	9	10	5555
9	Yakuza Arena	10	5	5555
10	Old Traford	11	9	8888
11	Baby Arena	12	1	9999
12	Le Stadia	13	8	6785
13	Stadium Tilatte Arena De Manuela	25	19	9999
\.

COPY team (team_id, team_name, team_couch) FROM stdin;
6	Comrade Putin	12
7	All Elizabeth	16
8	France Le Baseball	15
9	Kayserigücü	13
10	Ninjas	14
11	Cool Bros	14
12	Sexy Stylez	16
13	Le Le Le	15
14	Cyka	12
15	Russian Nuke	12
16	ISIS Paris	15
17	Pastırmaspor	13
18	Tren Gelir Yan Gelir	14
19	Putinspor	12
20	Erdoğanspor	17
21	Trabzonspor	13
22	Fenerbahçe	16
23	Şekerspor	18
24	şuhutspor	17
25	Tilattespor	12
\.

COPY team_stat (team_stat_id, team_stat_name, team_stat_run, team_stat_hit, team_stat_save, team_stat_win, team_stat_draw, team_stat_loss) FROM stdin;
1	6	2	2	1	0	0	2
2	25	66	66	66	0	0	0
\.

COPY tournament (tournament_id, tournament_name, tournament_matches, tournament_start_date, tournament_end_date, tournament_country, tournament_prize) FROM stdin;
3	The Grand Tournament	3	2010-10-10	2014-12-12	8	15000
4	Russian Warfare	100	2015-10-10	2020-12-12	9	500000
6	Westeros Grand Tournament	22	2016-06-05	2016-08-08	14	100000
\.

COPY users (user_id, user_name, password_hash, user_email, is_admin) FROM stdin;
1	testuser	$2a$12$rs1d2XYC7fNifoyBLU/8.uRq5jJvZDnmq/R8QnS/7Fa.bAnx0cA5u	test@test.com	f
2	akgunfu	$2a$12$96tF5LxXSRfbNhw/Om6SYu300J8k.qe.qnTwx5s3qmsJXdtpzd/P.	akgunfu@dball.net	t
3	turalog	$2a$12$8xndPYVxCbvdex7tHd8Lzu5o3onyhv8Wigvq2WwTtjxTAJgCS4T0y	turalog@dball.net	f
4	ozyar	$2a$12$u6Latb5gsgNVcehSrnOuT.nM2NhcCaBX3i7DV1Mki6FdV9NaD5Q66	ozyar@dball.net	t
5	sekermer	$2a$12$CNcsflTMZgO/sSt1V3tDoOMkQnb3UwiBO0ElNe4Gil44XQ6ISnU52	sekermer@dball.net	t
\.