import sqlite3


DB_NAME = 'obe_lesson_planner.db'


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # -------------------------
    # COURSES
    # -------------------------
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            programme TEXT NOT NULL,
            course_code TEXT NOT NULL,
            course_title TEXT NOT NULL,
            credit_hours INTEGER NOT NULL
        )
    ''')

    # -------------------------
    # PROGRAMME LEARNING OUTCOMES
    # -------------------------
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            programme TEXT NOT NULL,
            plo_code TEXT NOT NULL,
            description TEXT NOT NULL
        )
    ''')

    # -------------------------
    # COURSE LEARNING OUTCOMES
    # -------------------------
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            clo_code TEXT NOT NULL,
            description TEXT NOT NULL,
            bloom_level TEXT NOT NULL,
            plo_id INTEGER,
            FOREIGN KEY (course_id) REFERENCES courses(id),
            FOREIGN KEY (plo_id) REFERENCES plos(id)
        )
    ''')

    conn.commit()
    conn.close()


# =========================================================
# COURSE FUNCTIONS
# =========================================================

def add_course(programme, course_code, course_title, credit_hours):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO courses
        (programme, course_code, course_title, credit_hours)
        VALUES (?, ?, ?, ?)
        ''',
        (
            programme,
            course_code,
            course_title,
            credit_hours
        )
    )

    conn.commit()
    conn.close()


def get_courses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT *
        FROM courses
        ORDER BY programme, course_title
        '''
    )

    rows = cursor.fetchall()
    conn.close()

    return rows


# =========================================================
# PLO FUNCTIONS
# =========================================================

def add_plo(programme, plo_code, description):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO plos
        (programme, plo_code, description)
        VALUES (?, ?, ?)
        ''',
        (
            programme,
            plo_code,
            description
        )
    )

    conn.commit()
    conn.close()


def get_plos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT *
        FROM plos
        ORDER BY programme, plo_code
        '''
    )

    rows = cursor.fetchall()
    conn.close()

    return rows


# =========================================================
# CLO FUNCTIONS
# =========================================================

def add_clo(
    course_id,
    clo_code,
    description,
    bloom_level,
    plo_id
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO clos
        (
            course_id,
            clo_code,
            description,
            bloom_level,
            plo_id
        )
        VALUES (?, ?, ?, ?, ?)
        ''',
        (
            course_id,
            clo_code,
            description,
            bloom_level,
            plo_id
        )
    )

    conn.commit()
    conn.close()


def get_clos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT
            clos.id,
            clos.clo_code,
            clos.description,
            clos.bloom_level,
            courses.course_title,
            courses.course_code,
            plos.plo_code
        FROM clos
        JOIN courses
            ON clos.course_id = courses.id
        LEFT JOIN plos
            ON clos.plo_id = plos.id
        ORDER BY courses.course_title, clos.clo_code
        '''
    )

    rows = cursor.fetchall()
    conn.close()

    return rows