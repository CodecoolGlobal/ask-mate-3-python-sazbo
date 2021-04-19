--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

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
-- Name: ask_mate_db; Type: DATABASE; Schema: -; Owner: jakus
--

CREATE DATABASE ask_mate_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE ask_mate_db OWNER TO jakus;

\connect ask_mate_db

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
-- Name: answer; Type: TABLE; Schema: public; Owner: jakus
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    submission_time integer,
    vote_number integer,
    message text,
    image text,
    question_id integer
);


ALTER TABLE public.answer OWNER TO jakus;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: jakus
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO jakus;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jakus
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: jakus
--

CREATE TABLE public.comment (
    id integer NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time text,
    edited_number integer
);


ALTER TABLE public.comment OWNER TO jakus;

--
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: jakus
--

CREATE SEQUENCE public.comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO jakus;

--
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jakus
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: jakus
--

CREATE TABLE public.question (
    id integer NOT NULL,
    submission_time integer,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text
);


ALTER TABLE public.question OWNER TO jakus;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: jakus
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO jakus;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jakus
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: question_tag; Type: TABLE; Schema: public; Owner: jakus
--

CREATE TABLE public.question_tag (
    question_id integer,
    tag_id integer
);


ALTER TABLE public.question_tag OWNER TO jakus;

--
-- Name: tag; Type: TABLE; Schema: public; Owner: jakus
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.tag OWNER TO jakus;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: jakus
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO jakus;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: jakus
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: comment id; Type: DEFAULT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: jakus
--

INSERT INTO public.answer VALUES (1, 123, 1, 'asd', 'asd.jpg', 1);


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: jakus
--

INSERT INTO public.comment VALUES (1, 1, 1, 'comment', '123', 0);


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: jakus
--

INSERT INTO public.question VALUES (1, 123, 1, 2, 'asd', 'Lorem Ipsum', 'asd.jpg');


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: jakus
--

INSERT INTO public.question_tag VALUES (1, 1);


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: jakus
--

INSERT INTO public.tag VALUES (1, 'python');


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jakus
--

SELECT pg_catalog.setval('public.answer_id_seq', 1, false);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jakus
--

SELECT pg_catalog.setval('public.comment_id_seq', 1, false);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jakus
--

SELECT pg_catalog.setval('public.question_id_seq', 1, false);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: jakus
--

SELECT pg_catalog.setval('public.tag_id_seq', 1, false);


--
-- Name: answer answer_pk; Type: CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_pk PRIMARY KEY (id);


--
-- Name: comment comment_pk; Type: CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_pk PRIMARY KEY (id);


--
-- Name: question question_pk; Type: CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_pk PRIMARY KEY (id);


--
-- Name: tag tag_pk; Type: CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pk PRIMARY KEY (id);


--
-- Name: answer answer_fk; Type: FK CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_fk FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: comment answer_fk; Type: FK CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT answer_fk FOREIGN KEY (answer_id) REFERENCES public.answer(id);


--
-- Name: comment comment_fk; Type: FK CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_fk FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag question_fk; Type: FK CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT question_fk FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag tag_fk; Type: FK CONSTRAINT; Schema: public; Owner: jakus
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT tag_fk FOREIGN KEY (tag_id) REFERENCES public.tag(id);


--
-- PostgreSQL database dump complete
--

