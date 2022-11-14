--
-- PostgreSQL database dump
--

-- Dumped from database version 15.0
-- Dumped by pg_dump version 15.0

-- Started on 2022-11-14 16:03:23

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3350 (class 0 OID 16409)
-- Dependencies: 218
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: user_sanic
--

COPY public."user" (id, username, is_admin) FROM stdin;
1	user_4	f
2	user_3	t
3	user_2	f
4	user_1	f
\.


--
-- TOC entry 3352 (class 0 OID 16416)
-- Dependencies: 220
-- Data for Name: account; Type: TABLE DATA; Schema: public; Owner: user_sanic
--

COPY public.account (id, balance, owner) FROM stdin;
\.


--
-- TOC entry 3346 (class 0 OID 16396)
-- Dependencies: 214
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: user_sanic
--

COPY public.alembic_version (version_num) FROM stdin;
3b885e7f9666
\.


--
-- TOC entry 3348 (class 0 OID 16402)
-- Dependencies: 216
-- Data for Name: good; Type: TABLE DATA; Schema: public; Owner: user_sanic
--

COPY public.good (id, name, price) FROM stdin;
1	good_5	800.99
2	good_4	555.77
3	good_3	333.99
4	good_2	222.22
5	good_1	111.01
\.


--
-- TOC entry 3354 (class 0 OID 16428)
-- Dependencies: 222
-- Data for Name: transaction; Type: TABLE DATA; Schema: public; Owner: user_sanic
--

COPY public.transaction (id, date, amount, account) FROM stdin;
\.


--
-- TOC entry 3360 (class 0 OID 0)
-- Dependencies: 219
-- Name: account_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user_sanic
--

SELECT pg_catalog.setval('public.account_id_seq', 1, false);


--
-- TOC entry 3361 (class 0 OID 0)
-- Dependencies: 215
-- Name: good_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user_sanic
--

SELECT pg_catalog.setval('public.good_id_seq', 5, true);


--
-- TOC entry 3362 (class 0 OID 0)
-- Dependencies: 221
-- Name: transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user_sanic
--

SELECT pg_catalog.setval('public.transaction_id_seq', 1, false);


--
-- TOC entry 3363 (class 0 OID 0)
-- Dependencies: 217
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user_sanic
--

SELECT pg_catalog.setval('public.user_id_seq', 4, true);


-- Completed on 2022-11-14 16:03:23

--
-- PostgreSQL database dump complete
--

