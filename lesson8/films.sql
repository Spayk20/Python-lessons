--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

-- Started on 2021-05-09 21:47:18

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16429)
-- Name: actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actors (
    num integer,
    name text
);


ALTER TABLE public.actors OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16417)
-- Name: movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movies (
    num integer,
    title text
);


ALTER TABLE public.movies OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 16423)
-- Name: producers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.producers (
    num integer,
    name text
);


ALTER TABLE public.producers OWNER TO postgres;

--
-- TOC entry 2991 (class 0 OID 16429)
-- Dependencies: 202
-- Data for Name: actors; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2989 (class 0 OID 16417)
-- Dependencies: 200
-- Data for Name: movies; Type: TABLE DATA; Schema: public; Owner: postgres
--



--
-- TOC entry 2990 (class 0 OID 16423)
-- Dependencies: 201
-- Data for Name: producers; Type: TABLE DATA; Schema: public; Owner: postgres
--



-- Completed on 2021-05-09 21:47:20

--
-- PostgreSQL database dump complete
--

