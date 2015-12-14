--
-- PostgreSQL database dump
--

-- Dumped from database version 9.3.6
-- Dumped by pg_dump version 9.4.5
-- Started on 2015-12-14 02:34:21

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 210 (class 3079 OID 11789)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 3215 (class 0 OID 0)
-- Dependencies: 210
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- TOC entry 209 (class 3079 OID 36851)
-- Name: plv8; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plv8 WITH SCHEMA pg_catalog;


--
-- TOC entry 3216 (class 0 OID 0)
-- Dependencies: 209
-- Name: EXTENSION plv8; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plv8 IS 'PL/JavaScript (v8) trusted procedural language';


--
-- TOC entry 218 (class 3079 OID 35876)
-- Name: btree_gin; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS btree_gin WITH SCHEMA public;


--
-- TOC entry 3217 (class 0 OID 0)
-- Dependencies: 218
-- Name: EXTENSION btree_gin; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION btree_gin IS 'support for indexing common datatypes in GIN';


--
-- TOC entry 214 (class 3079 OID 36310)
-- Name: btree_gist; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS btree_gist WITH SCHEMA public;


--
-- TOC entry 3218 (class 0 OID 0)
-- Dependencies: 214
-- Name: EXTENSION btree_gist; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION btree_gist IS 'support for indexing common datatypes in GiST';


--
-- TOC entry 225 (class 3079 OID 35460)
-- Name: citext; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS citext WITH SCHEMA public;


--
-- TOC entry 3219 (class 0 OID 0)
-- Dependencies: 225
-- Name: EXTENSION citext; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION citext IS 'data type for case-insensitive character strings';


--
-- TOC entry 216 (class 3079 OID 36223)
-- Name: cube; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS cube WITH SCHEMA public;


--
-- TOC entry 3220 (class 0 OID 0)
-- Dependencies: 216
-- Name: EXTENSION cube; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION cube IS 'data type for multidimensional cubes';


--
-- TOC entry 231 (class 3079 OID 35187)
-- Name: dblink; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS dblink WITH SCHEMA public;


--
-- TOC entry 3221 (class 0 OID 0)
-- Dependencies: 231
-- Name: EXTENSION dblink; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dblink IS 'connect to other PostgreSQL databases from within a database';


--
-- TOC entry 219 (class 3079 OID 35871)
-- Name: dict_int; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS dict_int WITH SCHEMA public;


--
-- TOC entry 3222 (class 0 OID 0)
-- Dependencies: 219
-- Name: EXTENSION dict_int; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dict_int IS 'text search dictionary template for integers';


--
-- TOC entry 213 (class 3079 OID 36832)
-- Name: dict_xsyn; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS dict_xsyn WITH SCHEMA public;


--
-- TOC entry 3223 (class 0 OID 0)
-- Dependencies: 213
-- Name: EXTENSION dict_xsyn; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION dict_xsyn IS 'text search dictionary template for extended synonym processing';


--
-- TOC entry 215 (class 3079 OID 36295)
-- Name: earthdistance; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS earthdistance WITH SCHEMA public;


--
-- TOC entry 3224 (class 0 OID 0)
-- Dependencies: 215
-- Name: EXTENSION earthdistance; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION earthdistance IS 'calculate great-circle distances on the surface of the Earth';


--
-- TOC entry 226 (class 3079 OID 35449)
-- Name: fuzzystrmatch; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS fuzzystrmatch WITH SCHEMA public;


--
-- TOC entry 3225 (class 0 OID 0)
-- Dependencies: 226
-- Name: EXTENSION fuzzystrmatch; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION fuzzystrmatch IS 'determine similarities and distance between strings';


--
-- TOC entry 220 (class 3079 OID 35751)
-- Name: hstore; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS hstore WITH SCHEMA public;


--
-- TOC entry 3226 (class 0 OID 0)
-- Dependencies: 220
-- Name: EXTENSION hstore; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION hstore IS 'data type for storing sets of (key, value) pairs';


--
-- TOC entry 221 (class 3079 OID 35640)
-- Name: intarray; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS intarray WITH SCHEMA public;


--
-- TOC entry 3227 (class 0 OID 0)
-- Dependencies: 221
-- Name: EXTENSION intarray; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION intarray IS 'functions, operators, and index support for 1-D arrays of integers';


--
-- TOC entry 229 (class 3079 OID 35247)
-- Name: ltree; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS ltree WITH SCHEMA public;


--
-- TOC entry 3228 (class 0 OID 0)
-- Dependencies: 229
-- Name: EXTENSION ltree; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION ltree IS 'data type for hierarchical tree-like structures';


--
-- TOC entry 211 (class 3079 OID 36844)
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;


--
-- TOC entry 3229 (class 0 OID 0)
-- Dependencies: 211
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track execution statistics of all SQL statements executed';


--
-- TOC entry 222 (class 3079 OID 35589)
-- Name: pg_trgm; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_trgm WITH SCHEMA public;


--
-- TOC entry 3230 (class 0 OID 0)
-- Dependencies: 222
-- Name: EXTENSION pg_trgm; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_trgm IS 'text similarity measurement and index searching based on trigrams';


--
-- TOC entry 223 (class 3079 OID 35555)
-- Name: pgcrypto; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgcrypto WITH SCHEMA public;


--
-- TOC entry 3231 (class 0 OID 0)
-- Dependencies: 223
-- Name: EXTENSION pgcrypto; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgcrypto IS 'cryptographic functions';


--
-- TOC entry 217 (class 3079 OID 36221)
-- Name: pgrowlocks; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgrowlocks WITH SCHEMA public;


--
-- TOC entry 3232 (class 0 OID 0)
-- Dependencies: 217
-- Name: EXTENSION pgrowlocks; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgrowlocks IS 'show row-level locking information';


--
-- TOC entry 228 (class 3079 OID 35422)
-- Name: pgstattuple; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pgstattuple WITH SCHEMA public;


--
-- TOC entry 3233 (class 0 OID 0)
-- Dependencies: 228
-- Name: EXTENSION pgstattuple; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pgstattuple IS 'show tuple-level statistics';


--
-- TOC entry 227 (class 3079 OID 35428)
-- Name: tablefunc; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS tablefunc WITH SCHEMA public;


--
-- TOC entry 3234 (class 0 OID 0)
-- Dependencies: 227
-- Name: EXTENSION tablefunc; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION tablefunc IS 'functions that manipulate whole tables, including crosstab';


--
-- TOC entry 212 (class 3079 OID 36837)
-- Name: unaccent; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS unaccent WITH SCHEMA public;


--
-- TOC entry 3235 (class 0 OID 0)
-- Dependencies: 212
-- Name: EXTENSION unaccent; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION unaccent IS 'text search dictionary that removes accents';


--
-- TOC entry 224 (class 3079 OID 35544)
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- TOC entry 3236 (class 0 OID 0)
-- Dependencies: 224
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


--
-- TOC entry 230 (class 3079 OID 35233)
-- Name: xml2; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS xml2 WITH SCHEMA public;


--
-- TOC entry 3237 (class 0 OID 0)
-- Dependencies: 230
-- Name: EXTENSION xml2; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION xml2 IS 'XPath querying and XSLT';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 176 (class 1259 OID 863412)
-- Name: city; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE city (
    city_id integer NOT NULL,
    city_name text NOT NULL,
    city_coordinates text,
    city_population integer NOT NULL
);


ALTER TABLE city OWNER TO hcelelqm;

--
-- TOC entry 175 (class 1259 OID 863410)
-- Name: city_city_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE city_city_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE city_city_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3238 (class 0 OID 0)
-- Dependencies: 175
-- Name: city_city_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE city_city_id_seq OWNED BY city.city_id;


--
-- TOC entry 190 (class 1259 OID 863524)
-- Name: country; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE country (
    country_id integer NOT NULL,
    country_name text NOT NULL,
    country_population integer NOT NULL,
    capital integer NOT NULL
);


ALTER TABLE country OWNER TO hcelelqm;

--
-- TOC entry 189 (class 1259 OID 863522)
-- Name: country_country_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE country_country_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE country_country_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3239 (class 0 OID 0)
-- Dependencies: 189
-- Name: country_country_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE country_country_id_seq OWNED BY country.country_id;


--
-- TOC entry 192 (class 1259 OID 863535)
-- Name: league; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE league (
    league_id integer NOT NULL,
    league_name text NOT NULL,
    league_country integer NOT NULL,
    league_start_date date NOT NULL
);


ALTER TABLE league OWNER TO hcelelqm;

--
-- TOC entry 191 (class 1259 OID 863533)
-- Name: league_league_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE league_league_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE league_league_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3240 (class 0 OID 0)
-- Dependencies: 191
-- Name: league_league_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE league_league_id_seq OWNED BY league.league_id;


--
-- TOC entry 200 (class 1259 OID 863614)
-- Name: log; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE log (
    log_id integer NOT NULL,
    log_description text NOT NULL,
    log_author integer,
    log_time date NOT NULL
);


ALTER TABLE log OWNER TO hcelelqm;

--
-- TOC entry 199 (class 1259 OID 863612)
-- Name: log_log_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE log_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE log_log_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3241 (class 0 OID 0)
-- Dependencies: 199
-- Name: log_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE log_log_id_seq OWNED BY log.log_id;


--
-- TOC entry 202 (class 1259 OID 869878)
-- Name: matches; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE matches (
    match_id integer NOT NULL,
    match_team_1 integer,
    match_team_2 integer,
    match_league integer,
    match_stadium integer,
    match_referee integer,
    match_date date NOT NULL,
    match_team1_score integer NOT NULL,
    match_team2_score integer NOT NULL
);


ALTER TABLE matches OWNER TO hcelelqm;

--
-- TOC entry 201 (class 1259 OID 869876)
-- Name: matches_match_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE matches_match_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE matches_match_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3242 (class 0 OID 0)
-- Dependencies: 201
-- Name: matches_match_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE matches_match_id_seq OWNED BY matches.match_id;


--
-- TOC entry 186 (class 1259 OID 863490)
-- Name: penalty; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE penalty (
    penalty_id integer NOT NULL,
    penalty_type integer NOT NULL,
    penalty_given_person integer NOT NULL,
    penalty_given_date date NOT NULL
);


ALTER TABLE penalty OWNER TO hcelelqm;

--
-- TOC entry 185 (class 1259 OID 863488)
-- Name: penalty_penalty_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE penalty_penalty_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE penalty_penalty_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3243 (class 0 OID 0)
-- Dependencies: 185
-- Name: penalty_penalty_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE penalty_penalty_id_seq OWNED BY penalty.penalty_id;


--
-- TOC entry 184 (class 1259 OID 863477)
-- Name: penalty_type; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE penalty_type (
    id integer NOT NULL,
    penalty_type_name text NOT NULL
);


ALTER TABLE penalty_type OWNER TO hcelelqm;

--
-- TOC entry 183 (class 1259 OID 863475)
-- Name: penalty_type_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE penalty_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE penalty_type_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3244 (class 0 OID 0)
-- Dependencies: 183
-- Name: penalty_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE penalty_type_id_seq OWNED BY penalty_type.id;


--
-- TOC entry 180 (class 1259 OID 863438)
-- Name: person; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE person (
    person_id integer NOT NULL,
    person_name text NOT NULL,
    person_birth_date date NOT NULL,
    person_birth_location integer NOT NULL,
    person_type integer NOT NULL
);


ALTER TABLE person OWNER TO hcelelqm;

--
-- TOC entry 179 (class 1259 OID 863436)
-- Name: person_person_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE person_person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE person_person_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3245 (class 0 OID 0)
-- Dependencies: 179
-- Name: person_person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE person_person_id_seq OWNED BY person.person_id;


--
-- TOC entry 178 (class 1259 OID 863425)
-- Name: person_types; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE person_types (
    id integer NOT NULL,
    person_type_name text NOT NULL
);


ALTER TABLE person_types OWNER TO hcelelqm;

--
-- TOC entry 177 (class 1259 OID 863423)
-- Name: person_types_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE person_types_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE person_types_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3246 (class 0 OID 0)
-- Dependencies: 177
-- Name: person_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE person_types_id_seq OWNED BY person_types.id;


--
-- TOC entry 198 (class 1259 OID 863598)
-- Name: player; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE player (
    player_id integer NOT NULL,
    player_name text NOT NULL,
    player_team integer NOT NULL,
    player_goals integer NOT NULL
);


ALTER TABLE player OWNER TO hcelelqm;

--
-- TOC entry 197 (class 1259 OID 863596)
-- Name: player_player_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE player_player_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE player_player_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3247 (class 0 OID 0)
-- Dependencies: 197
-- Name: player_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE player_player_id_seq OWNED BY player.player_id;


--
-- TOC entry 206 (class 1259 OID 888822)
-- Name: popularity; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE popularity (
    popularity_id integer NOT NULL,
    team_name integer,
    most_popular_match integer,
    most_popular_player integer,
    supporters integer
);


ALTER TABLE popularity OWNER TO hcelelqm;

--
-- TOC entry 205 (class 1259 OID 888820)
-- Name: popularity_popularity_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE popularity_popularity_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE popularity_popularity_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3248 (class 0 OID 0)
-- Dependencies: 205
-- Name: popularity_popularity_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE popularity_popularity_id_seq OWNED BY popularity.popularity_id;


--
-- TOC entry 196 (class 1259 OID 863572)
-- Name: sponsorship; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE sponsorship (
    sponsorship_id integer NOT NULL,
    sponsorship_name text NOT NULL,
    sponsorship_start_date date NOT NULL,
    sponsorship_league integer,
    sponsorship_team integer,
    sponsorship_person integer
);


ALTER TABLE sponsorship OWNER TO hcelelqm;

--
-- TOC entry 195 (class 1259 OID 863570)
-- Name: sponsorship_sponsorship_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE sponsorship_sponsorship_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE sponsorship_sponsorship_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3249 (class 0 OID 0)
-- Dependencies: 195
-- Name: sponsorship_sponsorship_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE sponsorship_sponsorship_id_seq OWNED BY sponsorship.sponsorship_id;


--
-- TOC entry 194 (class 1259 OID 863551)
-- Name: stadium; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE stadium (
    stadium_id integer NOT NULL,
    stadium_name text NOT NULL,
    stadium_team integer NOT NULL,
    stadium_location integer NOT NULL,
    stadium_capacity integer NOT NULL
);


ALTER TABLE stadium OWNER TO hcelelqm;

--
-- TOC entry 193 (class 1259 OID 863549)
-- Name: stadium_stadium_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE stadium_stadium_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE stadium_stadium_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3250 (class 0 OID 0)
-- Dependencies: 193
-- Name: stadium_stadium_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE stadium_stadium_id_seq OWNED BY stadium.stadium_id;


--
-- TOC entry 182 (class 1259 OID 863461)
-- Name: team; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE team (
    team_id integer NOT NULL,
    team_name text NOT NULL,
    team_couch integer NOT NULL
);


ALTER TABLE team OWNER TO hcelelqm;

--
-- TOC entry 208 (class 1259 OID 895952)
-- Name: team_stat; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE team_stat (
    team_stat_id integer NOT NULL,
    team_stat_name integer NOT NULL,
    team_stat_run integer NOT NULL,
    team_stat_hit integer NOT NULL,
    team_stat_save integer NOT NULL,
    team_stat_win integer NOT NULL,
    team_stat_draw integer NOT NULL,
    team_stat_loss integer NOT NULL
);


ALTER TABLE team_stat OWNER TO hcelelqm;

--
-- TOC entry 207 (class 1259 OID 895950)
-- Name: team_stat_team_stat_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE team_stat_team_stat_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE team_stat_team_stat_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3251 (class 0 OID 0)
-- Dependencies: 207
-- Name: team_stat_team_stat_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE team_stat_team_stat_id_seq OWNED BY team_stat.team_stat_id;


--
-- TOC entry 181 (class 1259 OID 863459)
-- Name: team_team_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE team_team_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE team_team_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3252 (class 0 OID 0)
-- Dependencies: 181
-- Name: team_team_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE team_team_id_seq OWNED BY team.team_id;


--
-- TOC entry 204 (class 1259 OID 870025)
-- Name: tournament; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE tournament (
    tournament_id integer NOT NULL,
    tournament_name text NOT NULL,
    tournament_matches integer NOT NULL,
    tournament_start_date date NOT NULL,
    tournament_end_date date NOT NULL,
    tournament_country integer NOT NULL,
    tournament_prize integer NOT NULL
);


ALTER TABLE tournament OWNER TO hcelelqm;

--
-- TOC entry 203 (class 1259 OID 870023)
-- Name: tournament_tournament_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE tournament_tournament_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tournament_tournament_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3253 (class 0 OID 0)
-- Dependencies: 203
-- Name: tournament_tournament_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE tournament_tournament_id_seq OWNED BY tournament.tournament_id;


--
-- TOC entry 188 (class 1259 OID 863511)
-- Name: users; Type: TABLE; Schema: public; Owner: hcelelqm; Tablespace: 
--

CREATE TABLE users (
    user_id integer NOT NULL,
    user_name text NOT NULL,
    password_hash text NOT NULL,
    user_email text NOT NULL,
    is_admin boolean NOT NULL
);


ALTER TABLE users OWNER TO hcelelqm;

--
-- TOC entry 187 (class 1259 OID 863509)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: hcelelqm
--

CREATE SEQUENCE users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE users_user_id_seq OWNER TO hcelelqm;

--
-- TOC entry 3254 (class 0 OID 0)
-- Dependencies: 187
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: hcelelqm
--

ALTER SEQUENCE users_user_id_seq OWNED BY users.user_id;


--
-- TOC entry 2979 (class 2604 OID 863415)
-- Name: city_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY city ALTER COLUMN city_id SET DEFAULT nextval('city_city_id_seq'::regclass);


--
-- TOC entry 2986 (class 2604 OID 863527)
-- Name: country_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY country ALTER COLUMN country_id SET DEFAULT nextval('country_country_id_seq'::regclass);


--
-- TOC entry 2987 (class 2604 OID 863538)
-- Name: league_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY league ALTER COLUMN league_id SET DEFAULT nextval('league_league_id_seq'::regclass);


--
-- TOC entry 2991 (class 2604 OID 863617)
-- Name: log_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY log ALTER COLUMN log_id SET DEFAULT nextval('log_log_id_seq'::regclass);


--
-- TOC entry 2992 (class 2604 OID 869881)
-- Name: match_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY matches ALTER COLUMN match_id SET DEFAULT nextval('matches_match_id_seq'::regclass);


--
-- TOC entry 2984 (class 2604 OID 863493)
-- Name: penalty_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY penalty ALTER COLUMN penalty_id SET DEFAULT nextval('penalty_penalty_id_seq'::regclass);


--
-- TOC entry 2983 (class 2604 OID 863480)
-- Name: id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY penalty_type ALTER COLUMN id SET DEFAULT nextval('penalty_type_id_seq'::regclass);


--
-- TOC entry 2981 (class 2604 OID 863441)
-- Name: person_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY person ALTER COLUMN person_id SET DEFAULT nextval('person_person_id_seq'::regclass);


--
-- TOC entry 2980 (class 2604 OID 863428)
-- Name: id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY person_types ALTER COLUMN id SET DEFAULT nextval('person_types_id_seq'::regclass);


--
-- TOC entry 2990 (class 2604 OID 863601)
-- Name: player_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY player ALTER COLUMN player_id SET DEFAULT nextval('player_player_id_seq'::regclass);


--
-- TOC entry 2994 (class 2604 OID 888825)
-- Name: popularity_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY popularity ALTER COLUMN popularity_id SET DEFAULT nextval('popularity_popularity_id_seq'::regclass);


--
-- TOC entry 2989 (class 2604 OID 863575)
-- Name: sponsorship_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY sponsorship ALTER COLUMN sponsorship_id SET DEFAULT nextval('sponsorship_sponsorship_id_seq'::regclass);


--
-- TOC entry 2988 (class 2604 OID 863554)
-- Name: stadium_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY stadium ALTER COLUMN stadium_id SET DEFAULT nextval('stadium_stadium_id_seq'::regclass);


--
-- TOC entry 2982 (class 2604 OID 863464)
-- Name: team_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY team ALTER COLUMN team_id SET DEFAULT nextval('team_team_id_seq'::regclass);


--
-- TOC entry 2995 (class 2604 OID 895955)
-- Name: team_stat_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY team_stat ALTER COLUMN team_stat_id SET DEFAULT nextval('team_stat_team_stat_id_seq'::regclass);


--
-- TOC entry 2993 (class 2604 OID 870028)
-- Name: tournament_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY tournament ALTER COLUMN tournament_id SET DEFAULT nextval('tournament_tournament_id_seq'::regclass);


--
-- TOC entry 2985 (class 2604 OID 863514)
-- Name: user_id; Type: DEFAULT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY users ALTER COLUMN user_id SET DEFAULT nextval('users_user_id_seq'::regclass);


--
-- TOC entry 3175 (class 0 OID 863412)
-- Dependencies: 176
-- Data for Name: city; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3255 (class 0 OID 0)
-- Dependencies: 175
-- Name: city_city_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('city_city_id_seq', 21, true);


--
-- TOC entry 3189 (class 0 OID 863524)
-- Dependencies: 190
-- Data for Name: country; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3256 (class 0 OID 0)
-- Dependencies: 189
-- Name: country_country_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('country_country_id_seq', 17, true);


--
-- TOC entry 3191 (class 0 OID 863535)
-- Dependencies: 192
-- Data for Name: league; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY league (league_id, league_name, league_country, league_start_date) FROM stdin;
3	Süper Toto	7	1969-01-01
4	Ruski Comrade	9	1955-05-05
5	Rezzo Italiano	11	1965-05-06
6	Le League	8	1977-05-12
7	Elizabeth Premier	10	1967-12-01
\.


--
-- TOC entry 3257 (class 0 OID 0)
-- Dependencies: 191
-- Name: league_league_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('league_league_id_seq', 7, true);


--
-- TOC entry 3199 (class 0 OID 863614)
-- Dependencies: 200
-- Data for Name: log; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3258 (class 0 OID 0)
-- Dependencies: 199
-- Name: log_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('log_log_id_seq', 253, true);


--
-- TOC entry 3201 (class 0 OID 869878)
-- Dependencies: 202
-- Data for Name: matches; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3259 (class 0 OID 0)
-- Dependencies: 201
-- Name: matches_match_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('matches_match_id_seq', 16, true);


--
-- TOC entry 3185 (class 0 OID 863490)
-- Dependencies: 186
-- Data for Name: penalty; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY penalty (penalty_id, penalty_type, penalty_given_person, penalty_given_date) FROM stdin;
17	1	5	2015-10-11
\.


--
-- TOC entry 3260 (class 0 OID 0)
-- Dependencies: 185
-- Name: penalty_penalty_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('penalty_penalty_id_seq', 17, true);


--
-- TOC entry 3183 (class 0 OID 863477)
-- Dependencies: 184
-- Data for Name: penalty_type; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY penalty_type (id, penalty_type_name) FROM stdin;
1	Red Card
2	Yellow
\.


--
-- TOC entry 3261 (class 0 OID 0)
-- Dependencies: 183
-- Name: penalty_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('penalty_type_id_seq', 2, true);


--
-- TOC entry 3179 (class 0 OID 863438)
-- Dependencies: 180
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3262 (class 0 OID 0)
-- Dependencies: 179
-- Name: person_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('person_person_id_seq', 21, true);


--
-- TOC entry 3177 (class 0 OID 863425)
-- Dependencies: 178
-- Data for Name: person_types; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3263 (class 0 OID 0)
-- Dependencies: 177
-- Name: person_types_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('person_types_id_seq', 14, true);


--
-- TOC entry 3197 (class 0 OID 863598)
-- Dependencies: 198
-- Data for Name: player; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3264 (class 0 OID 0)
-- Dependencies: 197
-- Name: player_player_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('player_player_id_seq', 24, true);


--
-- TOC entry 3205 (class 0 OID 888822)
-- Dependencies: 206
-- Data for Name: popularity; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY popularity (popularity_id, team_name, most_popular_match, most_popular_player, supporters) FROM stdin;
11	6	7	12	2000000
12	17	10	21	100000000
\.


--
-- TOC entry 3265 (class 0 OID 0)
-- Dependencies: 205
-- Name: popularity_popularity_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('popularity_popularity_id_seq', 12, true);


--
-- TOC entry 3195 (class 0 OID 863572)
-- Dependencies: 196
-- Data for Name: sponsorship; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY sponsorship (sponsorship_id, sponsorship_name, sponsorship_start_date, sponsorship_league, sponsorship_team, sponsorship_person) FROM stdin;
3	Maret Sucuk	2111-01-01	5	7	8
4	Tİlattilaler	1985-02-25	4	25	5
5	Westboro Baptist Church	1995-04-12	3	16	17
\.


--
-- TOC entry 3266 (class 0 OID 0)
-- Dependencies: 195
-- Name: sponsorship_sponsorship_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('sponsorship_sponsorship_id_seq', 5, true);


--
-- TOC entry 3193 (class 0 OID 863551)
-- Dependencies: 194
-- Data for Name: stadium; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3267 (class 0 OID 0)
-- Dependencies: 193
-- Name: stadium_stadium_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('stadium_stadium_id_seq', 13, true);


--
-- TOC entry 3181 (class 0 OID 863461)
-- Dependencies: 182
-- Data for Name: team; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

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


--
-- TOC entry 3207 (class 0 OID 895952)
-- Dependencies: 208
-- Data for Name: team_stat; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY team_stat (team_stat_id, team_stat_name, team_stat_run, team_stat_hit, team_stat_save, team_stat_win, team_stat_draw, team_stat_loss) FROM stdin;
1	6	2	2	1	0	0	2
2	25	66	66	66	0	0	0
\.


--
-- TOC entry 3268 (class 0 OID 0)
-- Dependencies: 207
-- Name: team_stat_team_stat_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('team_stat_team_stat_id_seq', 2, true);


--
-- TOC entry 3269 (class 0 OID 0)
-- Dependencies: 181
-- Name: team_team_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('team_team_id_seq', 26, true);


--
-- TOC entry 3203 (class 0 OID 870025)
-- Dependencies: 204
-- Data for Name: tournament; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY tournament (tournament_id, tournament_name, tournament_matches, tournament_start_date, tournament_end_date, tournament_country, tournament_prize) FROM stdin;
3	The Grand Tournament	3	2010-10-10	2014-12-12	8	15000
4	Russian Warfare	100	2015-10-10	2020-12-12	9	500000
6	Westeros Grand Tournament	22	2016-06-05	2016-08-08	14	100000
\.


--
-- TOC entry 3270 (class 0 OID 0)
-- Dependencies: 203
-- Name: tournament_tournament_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('tournament_tournament_id_seq', 6, true);


--
-- TOC entry 3187 (class 0 OID 863511)
-- Dependencies: 188
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: hcelelqm
--

COPY users (user_id, user_name, password_hash, user_email, is_admin) FROM stdin;
1	testuser	$2a$12$rs1d2XYC7fNifoyBLU/8.uRq5jJvZDnmq/R8QnS/7Fa.bAnx0cA5u	test@test.com	f
2	akgunfu	$2a$12$96tF5LxXSRfbNhw/Om6SYu300J8k.qe.qnTwx5s3qmsJXdtpzd/P.	akgunfu@dball.net	t
3	turalog	$2a$12$8xndPYVxCbvdex7tHd8Lzu5o3onyhv8Wigvq2WwTtjxTAJgCS4T0y	turalog@dball.net	f
4	ozyar	$2a$12$u6Latb5gsgNVcehSrnOuT.nM2NhcCaBX3i7DV1Mki6FdV9NaD5Q66	ozyar@dball.net	t
5	sekermer	$2a$12$CNcsflTMZgO/sSt1V3tDoOMkQnb3UwiBO0ElNe4Gil44XQ6ISnU52	sekermer@dball.net	t
\.


--
-- TOC entry 3271 (class 0 OID 0)
-- Dependencies: 187
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: hcelelqm
--

SELECT pg_catalog.setval('users_user_id_seq', 5, true);


--
-- TOC entry 2997 (class 2606 OID 863422)
-- Name: city_city_name_key; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY city
    ADD CONSTRAINT city_city_name_key UNIQUE (city_name);


--
-- TOC entry 2999 (class 2606 OID 863420)
-- Name: city_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY city
    ADD CONSTRAINT city_pkey PRIMARY KEY (city_id);


--
-- TOC entry 3021 (class 2606 OID 863532)
-- Name: country_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_pkey PRIMARY KEY (country_id);


--
-- TOC entry 3023 (class 2606 OID 863543)
-- Name: league_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY league
    ADD CONSTRAINT league_pkey PRIMARY KEY (league_id);


--
-- TOC entry 3031 (class 2606 OID 863622)
-- Name: log_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY log
    ADD CONSTRAINT log_pkey PRIMARY KEY (log_id);


--
-- TOC entry 3033 (class 2606 OID 869883)
-- Name: matches_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY matches
    ADD CONSTRAINT matches_pkey PRIMARY KEY (match_id);


--
-- TOC entry 3015 (class 2606 OID 863498)
-- Name: penalty_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY penalty
    ADD CONSTRAINT penalty_pkey PRIMARY KEY (penalty_id);


--
-- TOC entry 3011 (class 2606 OID 863487)
-- Name: penalty_type_penalty_type_name_key; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY penalty_type
    ADD CONSTRAINT penalty_type_penalty_type_name_key UNIQUE (penalty_type_name);


--
-- TOC entry 3013 (class 2606 OID 863485)
-- Name: penalty_type_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY penalty_type
    ADD CONSTRAINT penalty_type_pkey PRIMARY KEY (id);


--
-- TOC entry 3005 (class 2606 OID 863448)
-- Name: person_person_name_key; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_person_name_key UNIQUE (person_name);


--
-- TOC entry 3007 (class 2606 OID 863446)
-- Name: person_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_pkey PRIMARY KEY (person_id);


--
-- TOC entry 3001 (class 2606 OID 863435)
-- Name: person_types_person_type_name_key; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY person_types
    ADD CONSTRAINT person_types_person_type_name_key UNIQUE (person_type_name);


--
-- TOC entry 3003 (class 2606 OID 863433)
-- Name: person_types_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY person_types
    ADD CONSTRAINT person_types_pkey PRIMARY KEY (id);


--
-- TOC entry 3029 (class 2606 OID 863606)
-- Name: player_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_pkey PRIMARY KEY (player_id);


--
-- TOC entry 3037 (class 2606 OID 888827)
-- Name: popularity_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY popularity
    ADD CONSTRAINT popularity_pkey PRIMARY KEY (popularity_id);


--
-- TOC entry 3027 (class 2606 OID 863580)
-- Name: sponsorship_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY sponsorship
    ADD CONSTRAINT sponsorship_pkey PRIMARY KEY (sponsorship_id);


--
-- TOC entry 3025 (class 2606 OID 863559)
-- Name: stadium_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY stadium
    ADD CONSTRAINT stadium_pkey PRIMARY KEY (stadium_id);


--
-- TOC entry 3039 (class 2606 OID 895959)
-- Name: team_name_unique; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY team_stat
    ADD CONSTRAINT team_name_unique UNIQUE (team_stat_name);


--
-- TOC entry 3009 (class 2606 OID 863469)
-- Name: team_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY team
    ADD CONSTRAINT team_pkey PRIMARY KEY (team_id);


--
-- TOC entry 3041 (class 2606 OID 895957)
-- Name: team_stat_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY team_stat
    ADD CONSTRAINT team_stat_pkey PRIMARY KEY (team_stat_id);


--
-- TOC entry 3035 (class 2606 OID 870033)
-- Name: tournament_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY tournament
    ADD CONSTRAINT tournament_pkey PRIMARY KEY (tournament_id);


--
-- TOC entry 3017 (class 2606 OID 863519)
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 3019 (class 2606 OID 863521)
-- Name: users_user_email_key; Type: CONSTRAINT; Schema: public; Owner: hcelelqm; Tablespace: 
--

ALTER TABLE ONLY users
    ADD CONSTRAINT users_user_email_key UNIQUE (user_email);


--
-- TOC entry 3047 (class 2606 OID 890133)
-- Name: country_capital_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY country
    ADD CONSTRAINT country_capital_fkey FOREIGN KEY (capital) REFERENCES city(city_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3048 (class 2606 OID 863544)
-- Name: league_league_country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY league
    ADD CONSTRAINT league_league_country_fkey FOREIGN KEY (league_country) REFERENCES country(country_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3055 (class 2606 OID 890318)
-- Name: log_log_author_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY log
    ADD CONSTRAINT log_log_author_fkey FOREIGN KEY (log_author) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3056 (class 2606 OID 890712)
-- Name: matches_match_league_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY matches
    ADD CONSTRAINT matches_match_league_fkey FOREIGN KEY (match_league) REFERENCES league(league_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3060 (class 2606 OID 890732)
-- Name: matches_match_referee_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY matches
    ADD CONSTRAINT matches_match_referee_fkey FOREIGN KEY (match_referee) REFERENCES person(person_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3059 (class 2606 OID 890727)
-- Name: matches_match_stadium_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY matches
    ADD CONSTRAINT matches_match_stadium_fkey FOREIGN KEY (match_stadium) REFERENCES stadium(stadium_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3058 (class 2606 OID 890722)
-- Name: matches_match_team_1_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY matches
    ADD CONSTRAINT matches_match_team_1_fkey FOREIGN KEY (match_team_1) REFERENCES team(team_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3057 (class 2606 OID 890717)
-- Name: matches_match_team_2_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY matches
    ADD CONSTRAINT matches_match_team_2_fkey FOREIGN KEY (match_team_2) REFERENCES team(team_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3046 (class 2606 OID 863504)
-- Name: penalty_penalty_given_person_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY penalty
    ADD CONSTRAINT penalty_penalty_given_person_fkey FOREIGN KEY (penalty_given_person) REFERENCES person(person_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3045 (class 2606 OID 863499)
-- Name: penalty_penalty_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY penalty
    ADD CONSTRAINT penalty_penalty_type_fkey FOREIGN KEY (penalty_type) REFERENCES penalty_type(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3042 (class 2606 OID 863449)
-- Name: person_person_birth_location_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_person_birth_location_fkey FOREIGN KEY (person_birth_location) REFERENCES city(city_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3043 (class 2606 OID 863454)
-- Name: person_person_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY person
    ADD CONSTRAINT person_person_type_fkey FOREIGN KEY (person_type) REFERENCES person_types(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3054 (class 2606 OID 863607)
-- Name: player_team_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY player
    ADD CONSTRAINT player_team_fkey FOREIGN KEY (player_team) REFERENCES team(team_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3063 (class 2606 OID 888833)
-- Name: popularity_most_popular_match_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY popularity
    ADD CONSTRAINT popularity_most_popular_match_fkey FOREIGN KEY (most_popular_match) REFERENCES matches(match_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3064 (class 2606 OID 888838)
-- Name: popularity_most_popular_player_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY popularity
    ADD CONSTRAINT popularity_most_popular_player_fkey FOREIGN KEY (most_popular_player) REFERENCES person(person_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3062 (class 2606 OID 888828)
-- Name: popularity_team_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY popularity
    ADD CONSTRAINT popularity_team_name_fkey FOREIGN KEY (team_name) REFERENCES team(team_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3051 (class 2606 OID 863581)
-- Name: sponsorship_sponsorship_league_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY sponsorship
    ADD CONSTRAINT sponsorship_sponsorship_league_fkey FOREIGN KEY (sponsorship_league) REFERENCES league(league_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3053 (class 2606 OID 863591)
-- Name: sponsorship_sponsorship_person_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY sponsorship
    ADD CONSTRAINT sponsorship_sponsorship_person_fkey FOREIGN KEY (sponsorship_person) REFERENCES person(person_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3052 (class 2606 OID 863586)
-- Name: sponsorship_sponsorship_team_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY sponsorship
    ADD CONSTRAINT sponsorship_sponsorship_team_fkey FOREIGN KEY (sponsorship_team) REFERENCES team(team_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3049 (class 2606 OID 863560)
-- Name: stadium_stadium_location_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY stadium
    ADD CONSTRAINT stadium_stadium_location_fkey FOREIGN KEY (stadium_location) REFERENCES city(city_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3050 (class 2606 OID 863565)
-- Name: stadium_stadium_team_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY stadium
    ADD CONSTRAINT stadium_stadium_team_fkey FOREIGN KEY (stadium_team) REFERENCES team(team_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3044 (class 2606 OID 863470)
-- Name: team_couch_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY team
    ADD CONSTRAINT team_couch_fkey FOREIGN KEY (team_couch) REFERENCES person(person_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3065 (class 2606 OID 895960)
-- Name: team_stat_name_stat_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY team_stat
    ADD CONSTRAINT team_stat_name_stat_name_fkey FOREIGN KEY (team_stat_name) REFERENCES team(team_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3061 (class 2606 OID 870034)
-- Name: tournament_country_fkey; Type: FK CONSTRAINT; Schema: public; Owner: hcelelqm
--

ALTER TABLE ONLY tournament
    ADD CONSTRAINT tournament_country_fkey FOREIGN KEY (tournament_country) REFERENCES country(country_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3214 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2015-12-14 02:35:57

--
-- PostgreSQL database dump complete
--

