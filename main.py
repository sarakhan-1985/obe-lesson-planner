from nicegui import ui
import os

from database import (
    create_tables,
    add_course,
    get_courses,
    add_plo,
    get_plos,
    add_clo,
    get_clos,
)

# =========================================================
# DATABASE
# =========================================================

create_tables()


# =========================================================
# HEADER / NAVIGATION
# =========================================================

def top_header():
    with ui.header().classes('items-center justify-between'):

        ui.label('OBE Lesson Planning Assistant').classes(
            'text-xl font-bold'
        )

        with ui.row().classes('gap-2'):

            ui.button(
                'Dashboard',
                on_click=lambda: ui.navigate.to('/')
            ).props('flat')

            ui.button(
                'Course Setup',
                on_click=lambda: ui.navigate.to('/course-setup')
            ).props('flat')

            ui.button(
                'PLOs & CLOs',
                on_click=lambda: ui.navigate.to('/outcomes')
            ).props('flat')

            ui.button(
                'Lesson Planner',
                on_click=lambda: ui.navigate.to('/lesson-planner')
            ).props('flat')

            ui.button(
                'Saved Plans',
                on_click=lambda: ui.navigate.to('/saved-plans')
            ).props('flat')


# =========================================================
# DASHBOARD
# =========================================================

@ui.page('/')
def dashboard():

    top_header()

    with ui.column().classes(
        'w-full max-w-6xl mx-auto p-8 gap-6'
    ):

        ui.label(
            'Dashboard'
        ).classes(
            'text-3xl font-bold'
        )

        ui.label(
            'Welcome to the OBE Lesson Planning Assistant.'
        ).classes(
            'text-lg'
        )

        ui.label(
            'Design constructively aligned lessons by connecting '
            'PLOs, CLOs, Bloom’s Taxonomy, teaching activities, '
            'assessment and evaluation.'
        )

        ui.separator()

        with ui.row().classes(
            'w-full gap-6 flex-wrap'
        ):

            # COURSE SETUP
            with ui.card().classes('w-64 p-5'):

                ui.icon(
                    'school',
                    size='40px'
                )

                ui.label(
                    'Course Setup'
                ).classes(
                    'text-xl font-semibold'
                )

                ui.label(
                    'Add programmes and courses.'
                )

                ui.button(
                    'Open',
                    on_click=lambda: ui.navigate.to('/course-setup')
                )

            # PLO CLO
            with ui.card().classes('w-64 p-5'):

                ui.icon(
                    'account_tree',
                    size='40px'
                )

                ui.label(
                    'PLOs & CLOs'
                ).classes(
                    'text-xl font-semibold'
                )

                ui.label(
                    'Define and map learning outcomes.'
                )

                ui.button(
                    'Open',
                    on_click=lambda: ui.navigate.to('/outcomes')
                )

            # LESSON PLANNER
            with ui.card().classes('w-64 p-5'):

                ui.icon(
                    'edit_note',
                    size='40px'
                )

                ui.label(
                    'Create OBE Lesson Plan'
                ).classes(
                    'text-xl font-semibold'
                )

                ui.label(
                    'Design an aligned lesson plan.'
                )

                ui.button(
                    'Start Lesson Planning',
                    icon='arrow_forward',
                    on_click=lambda: ui.navigate.to('/lesson-planner')
                )

            # SAVED PLANS
            with ui.card().classes('w-64 p-5'):

                ui.icon(
                    'folder',
                    size='40px'
                )

                ui.label(
                    'Saved Plans'
                ).classes(
                    'text-xl font-semibold'
                )

                ui.label(
                    'Review saved lesson plans.'
                )

                ui.button(
                    'Open',
                    on_click=lambda: ui.navigate.to('/saved-plans')
                )


# =========================================================
# COURSE SETUP
# =========================================================

@ui.page('/course-setup')
def course_setup():

    top_header()

    with ui.column().classes(
        'w-full max-w-5xl mx-auto p-8 gap-6'
    ):

        ui.button(
            'Back to Dashboard',
            icon='arrow_back',
            on_click=lambda: ui.navigate.to('/')
        ).props('outline')

        ui.label(
            'Course Setup'
        ).classes(
            'text-3xl font-bold'
        )

        ui.label(
            'Create programmes and courses for OBE lesson planning.'
        )

        with ui.card().classes(
            'w-full p-6 gap-4'
        ):

            ui.label(
                'Add Course'
            ).classes(
                'text-xl font-semibold'
            )

            programme = ui.input(
                label='Programme Name',
                placeholder='e.g. BS Computer Science'
            ).classes('w-full')

            course_code = ui.input(
                label='Course Code',
                placeholder='e.g. SS1001'
            ).classes('w-full')

            course_title = ui.input(
                label='Course Title',
                placeholder='e.g. Functional English'
            ).classes('w-full')

            credit_hours = ui.number(
                label='Credit Hours',
                value=3,
                min=1,
                max=6
            )

            def save_course():

                if not programme.value:
                    ui.notify(
                        'Please enter programme name.',
                        type='negative'
                    )
                    return

                if not course_code.value:
                    ui.notify(
                        'Please enter course code.',
                        type='negative'
                    )
                    return

                if not course_title.value:
                    ui.notify(
                        'Please enter course title.',
                        type='negative'
                    )
                    return

                add_course(
                    programme.value,
                    course_code.value,
                    course_title.value,
                    int(credit_hours.value)
                )

                ui.notify(
                    'Course saved successfully!',
                    type='positive'
                )

                programme.value = ''
                course_code.value = ''
                course_title.value = ''
                credit_hours.value = 3

                course_table.refresh()

            ui.button(
                'Save Course',
                icon='save',
                on_click=save_course
            )

        # SAVED COURSES

        @ui.refreshable
        def course_table():

            courses = get_courses()

            ui.label(
                'Saved Courses'
            ).classes(
                'text-xl font-semibold'
            )

            columns = [
                {
                    'name': 'programme',
                    'label': 'Programme',
                    'field': 'programme'
                },
                {
                    'name': 'code',
                    'label': 'Course Code',
                    'field': 'code'
                },
                {
                    'name': 'title',
                    'label': 'Course Title',
                    'field': 'title'
                },
                {
                    'name': 'credit_hours',
                    'label': 'Credit Hours',
                    'field': 'credit_hours'
                },
            ]

            rows = []

            for course in courses:

                rows.append(
                    {
                        'programme': course['programme'],
                        'code': course['course_code'],
                        'title': course['course_title'],
                        'credit_hours': course['credit_hours']
                    }
                )

            ui.table(
                columns=columns,
                rows=rows
            ).classes('w-full')

        course_table()


# =========================================================
# PLOs AND CLOs
# =========================================================

@ui.page('/outcomes')
def outcomes():

    top_header()

    with ui.column().classes(
        'w-full max-w-6xl mx-auto p-8 gap-6'
    ):

        ui.button(
            'Back to Dashboard',
            icon='arrow_back',
            on_click=lambda: ui.navigate.to('/')
        ).props('outline')

        ui.label(
            'PLOs & CLOs'
        ).classes(
            'text-3xl font-bold'
        )

        ui.label(
            'Define Programme Learning Outcomes, '
            'Course Learning Outcomes and their alignment.'
        )

        # =================================================
        # PLO SECTION
        # =================================================

        with ui.card().classes(
            'w-full p-6 gap-4'
        ):

            ui.label(
                'Programme Learning Outcomes'
            ).classes(
                'text-xl font-semibold'
            )

            plo_programme = ui.input(
                label='Programme',
                placeholder='e.g. BS Computer Science'
            ).classes('w-full')

            plo_code = ui.input(
                label='PLO Code',
                placeholder='e.g. PLO 1'
            ).classes('w-full')

            plo_description = ui.textarea(
                label='PLO Description',
                placeholder='Enter the programme learning outcome'
            ).classes('w-full')

            def save_plo():

                if not plo_programme.value:
                    ui.notify(
                        'Please enter the programme.',
                        type='negative'
                    )
                    return

                if not plo_code.value:
                    ui.notify(
                        'Please enter a PLO code.',
                        type='negative'
                    )
                    return

                if not plo_description.value:
                    ui.notify(
                        'Please enter the PLO description.',
                        type='negative'
                    )
                    return

                add_plo(
                    plo_programme.value,
                    plo_code.value,
                    plo_description.value
                )

                ui.notify(
                    'PLO saved successfully!',
                    type='positive'
                )

                plo_code.value = ''
                plo_description.value = ''

                plo_table.refresh()

            ui.button(
                'Add PLO',
                icon='add',
                on_click=save_plo
            )

        # PLO TABLE

        @ui.refreshable
        def plo_table():

            plos = get_plos()

            ui.label(
                'Saved PLOs'
            ).classes(
                'text-xl font-semibold'
            )

            columns = [
                {
                    'name': 'programme',
                    'label': 'Programme',
                    'field': 'programme'
                },
                {
                    'name': 'code',
                    'label': 'PLO',
                    'field': 'code'
                },
                {
                    'name': 'description',
                    'label': 'Description',
                    'field': 'description'
                },
            ]

            rows = []

            for plo in plos:

                rows.append(
                    {
                        'programme': plo['programme'],
                        'code': plo['plo_code'],
                        'description': plo['description']
                    }
                )

            ui.table(
                columns=columns,
                rows=rows
            ).classes('w-full')

        plo_table()

        # =================================================
        # CLO SECTION
        # =================================================

        with ui.card().classes(
            'w-full p-6 gap-4'
        ):

            ui.label(
                'Course Learning Outcomes'
            ).classes(
                'text-xl font-semibold'
            )

            courses = get_courses()

            course_options = {
                course['id']:
                    f"{course['course_code']} - "
                    f"{course['course_title']}"
                for course in courses
            }

            clo_course = ui.select(
                options=course_options,
                label='Select Course'
            ).classes('w-full')

            clo_code = ui.input(
                label='CLO Code',
                placeholder='e.g. CLO 1'
            ).classes('w-full')

            clo_description = ui.textarea(
                label='CLO Description',
                placeholder='Enter the course learning outcome'
            ).classes('w-full')

            bloom_level = ui.select(
                [
                    'Remember',
                    'Understand',
                    'Apply',
                    'Analyze',
                    'Evaluate',
                    'Create'
                ],
                label="Bloom's Taxonomy Level"
            ).classes('w-full')

            plos = get_plos()

            plo_options = {
                plo['id']:
                    f"{plo['plo_code']} - "
                    f"{plo['description']}"
                for plo in plos
            }

            mapped_plo = ui.select(
                options=plo_options,
                label='Map CLO to PLO'
            ).classes('w-full')

            def save_clo():

                if not clo_course.value:
                    ui.notify(
                        'Please select a course.',
                        type='negative'
                    )
                    return

                if not clo_code.value:
                    ui.notify(
                        'Please enter a CLO code.',
                        type='negative'
                    )
                    return

                if not clo_description.value:
                    ui.notify(
                        'Please enter the CLO description.',
                        type='negative'
                    )
                    return

                if not bloom_level.value:
                    ui.notify(
                        "Please select Bloom's level.",
                        type='negative'
                    )
                    return

                if not mapped_plo.value:
                    ui.notify(
                        'Please map the CLO to a PLO.',
                        type='negative'
                    )
                    return

                add_clo(
                    clo_course.value,
                    clo_code.value,
                    clo_description.value,
                    bloom_level.value,
                    mapped_plo.value
                )

                ui.notify(
                    'CLO saved successfully!',
                    type='positive'
                )

                clo_code.value = ''
                clo_description.value = ''
                bloom_level.value = None
                mapped_plo.value = None

                clo_table.refresh()

            ui.button(
                'Add CLO',
                icon='add',
                on_click=save_clo
            )

        # CLO TABLE

        @ui.refreshable
        def clo_table():

            clos = get_clos()

            ui.label(
                'Saved CLOs'
            ).classes(
                'text-xl font-semibold'
            )

            columns = [
                {
                    'name': 'course',
                    'label': 'Course',
                    'field': 'course'
                },
                {
                    'name': 'clo',
                    'label': 'CLO',
                    'field': 'clo'
                },
                {
                    'name': 'description',
                    'label': 'Description',
                    'field': 'description'
                },
                {
                    'name': 'bloom',
                    'label': "Bloom's Level",
                    'field': 'bloom'
                },
                {
                    'name': 'plo',
                    'label': 'Mapped PLO',
                    'field': 'plo'
                },
            ]

            rows = []

            for clo in clos:

                rows.append(
                    {
                        'course': clo['course_title'],
                        'clo': clo['clo_code'],
                        'description': clo['description'],
                        'bloom': clo['bloom_level'],
                        'plo': clo['plo_code']
                    }
                )

            ui.table(
                columns=columns,
                rows=rows
            ).classes('w-full')

        clo_table()


# =========================================================
# LESSON PLANNER
# =========================================================

@ui.page('/lesson-planner')
def lesson_planner():

    top_header()

    with ui.column().classes(
        'w-full max-w-6xl mx-auto p-8 gap-6'
    ):

        ui.button(
            'Back to Dashboard',
            icon='arrow_back',
            on_click=lambda: ui.navigate.to('/')
        ).props('outline')

        ui.label(
            'OBE Lesson Planner'
        ).classes(
            'text-3xl font-bold'
        )

        ui.label(
            'Develop a lesson aligned with an approved '
            'Course Learning Outcome.'
        )

        # -------------------------
        # COURSE
        # -------------------------

        courses = get_courses()

        course_options = {
            course['id']:
                f"{course['course_code']} - "
                f"{course['course_title']}"
            for course in courses
        }

        selected_course = ui.select(
            options=course_options,
            label='Select Course'
        ).classes('w-full')

        # -------------------------
        # CLO
        # -------------------------

        clos = get_clos()

        clo_options = {
            clo['id']:
                f"{clo['clo_code']} - "
                f"{clo['description']} "
                f"[{clo['bloom_level']}]"
            for clo in clos
        }

        selected_clo = ui.select(
            options=clo_options,
            label='Select CLO'
        ).classes('w-full')

        ui.separator()

        topic = ui.input(
            label='Lesson Topic',
            placeholder='e.g. Paraphrasing'
        ).classes('w-full')

        duration = ui.number(
            label='Lesson Duration (minutes)',
            value=60,
            min=10
        )

        lesson_outcome = ui.textarea(
            label='Lesson Learning Outcome',
            placeholder=(
                'By the end of the lesson, '
                'students will be able to...'
            )
        ).classes('w-full')

        teaching_method = ui.select(
            [
                'Interactive Lecture',
                'Discussion',
                'Guided Practice',
                'Think-Pair-Share',
                'Collaborative Learning',
                'Problem-Based Learning',
                'Case-Based Learning',
                'Project-Based Learning',
                'Flipped Learning'
            ],
            label='Teaching Method'
        ).classes('w-full')

        activity = ui.textarea(
            label='Teaching / Learning Activity',
            placeholder=(
                'Describe what the teacher '
                'and students will do.'
            )
        ).classes('w-full')

        assessment_method = ui.select(
            [
                'Quiz',
                'Worksheet',
                'Class Activity',
                'Presentation',
                'Written Task',
                'Reflection',
                'Peer Assessment',
                'Group Task',
                'Exit Ticket',
                'Project'
            ],
            label='Assessment Method'
        ).classes('w-full')

        assessment_task = ui.textarea(
            label='Assessment Task',
            placeholder=(
                'How will students demonstrate '
                'achievement of the CLO?'
            )
        ).classes('w-full')

        success_criterion = ui.input(
            label='Success Criterion',
            placeholder=(
                'e.g. 80% of students '
                'achieve at least 70%'
            )
        ).classes('w-full')

        evaluation = ui.textarea(
            label='Evaluation / Improvement Plan',
            placeholder=(
                'How will attainment be reviewed '
                'and improved?'
            )
        ).classes('w-full')

        with ui.row():

            ui.button(
                'Check OBE Alignment',
                icon='fact_check'
            )

            ui.button(
                'Save Lesson Plan',
                icon='save'
            )


# =========================================================
# SAVED PLANS
# =========================================================

@ui.page('/saved-plans')
def saved_plans():

    top_header()

    with ui.column().classes(
        'w-full max-w-6xl mx-auto p-8 gap-6'
    ):

        ui.button(
            'Back to Dashboard',
            icon='arrow_back',
            on_click=lambda: ui.navigate.to('/')
        ).props('outline')

        ui.label(
            'Saved Lesson Plans'
        ).classes(
            'text-3xl font-bold'
        )

        ui.label(
            'Saved lesson plans will appear here once '
            'lesson-plan storage is connected.'
        )


# =========================================================
# RUN APP
# =========================================================

ui.run(
    title='OBE Lesson Planning Assistant',
    host='0.0.0.0',
    port=int(os.environ.get('PORT', 8080)),
    reload=False
)