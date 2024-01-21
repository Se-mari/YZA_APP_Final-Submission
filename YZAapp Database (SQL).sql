-- This script was generated by the ERD tool in pgAdmin 4.
-- Please log an issue at https://redmine.postgresql.org/projects/pgadmin4/issues/new if you find any bugs, including reproduction steps.
BEGIN;


CREATE TABLE IF NOT EXISTS public.category
(
    category_id integer NOT NULL DEFAULT nextval('category_category_id_seq'::regclass),
    category_name character varying(64) COLLATE pg_catalog."default",
    category_description text COLLATE pg_catalog."default",
    category_delete_ind boolean DEFAULT false,
    CONSTRAINT category_pkey PRIMARY KEY (category_id)
);

CREATE TABLE IF NOT EXISTS public.customer
(
    customer_id integer NOT NULL DEFAULT nextval('customer_customer_id_seq'::regclass),
    customer_fname character varying(128) COLLATE pg_catalog."default",
    customer_lname character varying(128) COLLATE pg_catalog."default",
    customer_phone character varying(128) COLLATE pg_catalog."default",
    customer_email character varying(128) COLLATE pg_catalog."default",
    occupation_id integer,
    customer_delete_ind boolean DEFAULT false,
    CONSTRAINT customer_pkey PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS public.material
(
    material_id integer NOT NULL DEFAULT nextval('material_material_id_seq'::regclass),
    material_name character varying(32) COLLATE pg_catalog."default",
    category_id integer,
    in_stock integer,
    unit_price integer,
    reorder_point integer,
    material_delete_ind boolean DEFAULT false,
    CONSTRAINT material_pkey PRIMARY KEY (material_id)
);

CREATE TABLE IF NOT EXISTS public.occupation
(
    occupation_id integer NOT NULL DEFAULT nextval('occupation_occupation_id_seq'::regclass),
    occupation_name character varying(32) COLLATE pg_catalog."default",
    occupation_delete_ind boolean DEFAULT false,
    occupation_description character varying(128) COLLATE pg_catalog."default",
    CONSTRAINT occupation_pkey PRIMARY KEY (occupation_id)
);

CREATE TABLE IF NOT EXISTS public.payment_type
(
    type_id integer NOT NULL DEFAULT nextval('payment_type_type_id_seq'::regclass),
    type_name character varying(32) COLLATE pg_catalog."default",
    type_description character varying(128) COLLATE pg_catalog."default",
    type_delete_ind boolean DEFAULT false,
    CONSTRAINT payment_type_pkey PRIMARY KEY (type_id)
);

CREATE TABLE IF NOT EXISTS public.purchase_order
(
    purchase_id integer NOT NULL DEFAULT nextval('purchase_order_purchase_id_seq'::regclass),
    sales_invoice character varying(32) COLLATE pg_catalog."default",
    type_id integer,
    staff_id integer,
    amount integer,
    purchase_order_delete_ind boolean DEFAULT false,
    purchase_order_date timestamp without time zone,
    CONSTRAINT purchase_order_pkey PRIMARY KEY (purchase_id)
);

CREATE TABLE IF NOT EXISTS public.service
(
    service_id integer NOT NULL DEFAULT nextval('service_service_id_seq'::regclass),
    service_name character varying(32) COLLATE pg_catalog."default",
    service_description text COLLATE pg_catalog."default",
    service_price integer,
    quantity integer,
    material_id integer,
    service_delete_ind boolean DEFAULT false,
    CONSTRAINT service_pkey PRIMARY KEY (service_id)
);

CREATE TABLE IF NOT EXISTS public.staff
(
    staff_id integer NOT NULL DEFAULT nextval('staff_staff_id_seq'::regclass),
    staff_fname character varying(128) COLLATE pg_catalog."default",
    staff_lname character varying(128) COLLATE pg_catalog."default",
    staff_phone character varying(128) COLLATE pg_catalog."default",
    staff_email character varying(128) COLLATE pg_catalog."default",
    role_id integer,
    staff_delete_ind boolean DEFAULT false,
    CONSTRAINT staff_pkey PRIMARY KEY (staff_id)
);

CREATE TABLE IF NOT EXISTS public.staff_report
(
    report_id integer NOT NULL DEFAULT nextval('staff_report_report_id_seq'::regclass),
    report text COLLATE pg_catalog."default",
    staff_id integer,
    report_delete_ind boolean DEFAULT false,
    report_date timestamp without time zone,
    purchase_order_date timestamp without time zone,
    CONSTRAINT staff_report_pkey PRIMARY KEY (report_id)
);

CREATE TABLE IF NOT EXISTS public.staff_role
(
    role_id integer NOT NULL DEFAULT nextval('staff_role_role_id_seq'::regclass),
    role_name character varying(32) COLLATE pg_catalog."default",
    role_description character varying(32) COLLATE pg_catalog."default",
    staff_role_delete_ind boolean DEFAULT false,
    CONSTRAINT staff_role_pkey PRIMARY KEY (role_id)
);

CREATE TABLE IF NOT EXISTS public.status
(
    status_id integer NOT NULL DEFAULT nextval('status_status_id_seq'::regclass),
    status_name character varying(32) COLLATE pg_catalog."default",
    status_description text COLLATE pg_catalog."default",
    status_delete_ind boolean DEFAULT false,
    CONSTRAINT status_pkey PRIMARY KEY (status_id)
);

CREATE TABLE IF NOT EXISTS public.suppliers
(
    suppliers_id integer NOT NULL DEFAULT nextval('suppliers_suppliers_id_seq'::regclass),
    suppliers_name character varying(64) COLLATE pg_catalog."default",
    suppliers_phone character varying(32) COLLATE pg_catalog."default",
    suppliers_email character varying(64) COLLATE pg_catalog."default",
    suppliers_province character varying(64) COLLATE pg_catalog."default",
    suppliers_city character varying(64) COLLATE pg_catalog."default",
    suppliers_street character varying(64) COLLATE pg_catalog."default",
    suppliers_number character varying(64) COLLATE pg_catalog."default",
    suppliers_delete_ind boolean DEFAULT false,
    CONSTRAINT suppliers_pkey PRIMARY KEY (suppliers_id)
);

CREATE TABLE IF NOT EXISTS public.supplies
(
    supply_id integer NOT NULL DEFAULT nextval('supplies_supply_id_seq'::regclass),
    purchase_id integer,
    material_id integer,
    suppliers_id integer,
    quantity integer,
    supplies_delete_ind boolean DEFAULT false,
    CONSTRAINT supplies_pkey PRIMARY KEY (supply_id)
);

CREATE TABLE IF NOT EXISTS public.transaction
(
    transaction_id integer NOT NULL DEFAULT nextval('transaction_transaction_id_seq'::regclass),
    created_date timestamp without time zone,
    last_modified timestamp without time zone,
    amount integer,
    customer_id integer,
    staff_id integer,
    type_id integer,
    status_id integer,
    service_id integer,
    quantity integer,
    transaction_delete_ind boolean DEFAULT false,
    lead_time text COLLATE pg_catalog."default",
    CONSTRAINT transaction_pkey PRIMARY KEY (transaction_id)
);

CREATE TABLE IF NOT EXISTS public.users
(
    user_id integer NOT NULL DEFAULT nextval('users_user_id_seq'::regclass),
    user_name character varying(32) COLLATE pg_catalog."default",
    staff_id integer,
    user_password character varying(64) COLLATE pg_catalog."default" NOT NULL,
    user_modified_on timestamp without time zone DEFAULT now(),
    user_delete_ind boolean DEFAULT false,
    CONSTRAINT users_pkey PRIMARY KEY (user_id),
    CONSTRAINT users_user_name_key UNIQUE (user_name)
);

ALTER TABLE IF EXISTS public.customer
    ADD CONSTRAINT fk_occupation_id FOREIGN KEY (occupation_id)
    REFERENCES public.occupation (occupation_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.material
    ADD CONSTRAINT fk_category FOREIGN KEY (category_id)
    REFERENCES public.category (category_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.purchase_order
    ADD CONSTRAINT fk_payment_type FOREIGN KEY (type_id)
    REFERENCES public.payment_type (type_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.purchase_order
    ADD CONSTRAINT fk_staff FOREIGN KEY (staff_id)
    REFERENCES public.staff (staff_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.service
    ADD CONSTRAINT fk_material FOREIGN KEY (material_id)
    REFERENCES public.material (material_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.staff
    ADD CONSTRAINT fk_staff_role FOREIGN KEY (role_id)
    REFERENCES public.staff_role (role_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.staff_report
    ADD CONSTRAINT fk_staff FOREIGN KEY (staff_id)
    REFERENCES public.staff (staff_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.supplies
    ADD CONSTRAINT fk_material FOREIGN KEY (material_id)
    REFERENCES public.material (material_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.supplies
    ADD CONSTRAINT fk_purchase_order FOREIGN KEY (purchase_id)
    REFERENCES public.purchase_order (purchase_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.supplies
    ADD CONSTRAINT fk_suppliers FOREIGN KEY (suppliers_id)
    REFERENCES public.suppliers (suppliers_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.transaction
    ADD CONSTRAINT fk_customer FOREIGN KEY (customer_id)
    REFERENCES public.customer (customer_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.transaction
    ADD CONSTRAINT fk_payment_type FOREIGN KEY (type_id)
    REFERENCES public.payment_type (type_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.transaction
    ADD CONSTRAINT fk_service FOREIGN KEY (service_id)
    REFERENCES public.service (service_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.transaction
    ADD CONSTRAINT fk_staff FOREIGN KEY (staff_id)
    REFERENCES public.staff (staff_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.transaction
    ADD CONSTRAINT fk_status FOREIGN KEY (status_id)
    REFERENCES public.status (status_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.users
    ADD CONSTRAINT fk_staff FOREIGN KEY (staff_id)
    REFERENCES public.staff (staff_id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;

END;