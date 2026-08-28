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

    # -----------------------------------------------------
    # HERO SECTION
    # -----------------------------------------------------

    with ui.column().classes(
        'w-full items-center text-center p-10 gap-4'
    ).style(
        '''
        background: linear-gradient(
            135deg,
            #4338ca 0%,
            #7c3aed 48%,
            #db2777 100%
        );
        color: white;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.18);
        '''
    ):

        ui.icon(
            'auto_awesome',
            size='58px'
        )

        ui.label(
            'OBE Lesson Planning Assistant'
        ).classes(
            'text-4xl font-bold'
        )

        ui.label(
            'From Outcomes to Impact'
        ).classes(
            'text-2xl font-semibold'
        )

        ui.label(
            'Transform PLOs and CLOs into meaningful, aligned and '
            'measurable classroom experiences.'
        ).classes(
            'text-lg max-w-3xl'
        )

        ui.button(
            'Start Lesson Planning',
            icon='rocket_launch',
            on_click=lambda: ui.navigate.to('/lesson-planner')
        ).props(
            'unelevated rounded'
        ).classes(
            'q-mt-md text-lg'
        ).style(
            '''
            background-color: white;
            color: #5b21b6;
            font-weight: 700;
            padding: 8px 20px;
            '''
        )

    # -----------------------------------------------------
    # MAIN DASHBOARD CONTENT
    # -----------------------------------------------------

    with ui.column().classes(
        'w-full max-w-6xl mx-auto p-8 gap-8'
    ):

        ui.label(
            'Build Your OBE Lesson'
        ).classes(
            'text-3xl font-bold text-center'
        )

        ui.label(
            'Follow the OBE journey from programme outcomes '
            'to classroom assessment, evaluation and improvement.'
        ).classes(
            'text-center text-gray-600 text-lg'
        )

        # -------------------------------------------------
        # OBE ALIGNMENT FLOW
        # -------------------------------------------------

        with ui.card().classes(
            'w-full p-6'
        ).style(
            '''
            border-radius: 20px;
            background: linear-gradient(
                90deg,
                #f8fafc,
                #f5f3ff
            );
            '''
        ):

            ui.label(
                'The OBE Alignment Journey'
            ).classes(
                'text-xl font-bold text-center'
            )

            with ui.row().classes(
                'w-full justify-center items-center '
                'gap-3 flex-wrap q-mt-md'
            ):

                ui.badge(
                    'PLO',
                    color='indigo'
                ).classes(
                    'text-base p-3'
                )

                ui.icon(
                    'arrow_forward',
                    color='grey'
                )

                ui.badge(
                    'CLO',
                    color='purple'
                ).classes(
                    'text-base p-3'
                )

                ui.icon(
                    'arrow_forward',
                    color='grey'
                )

                ui.badge(
                    'Learning Activity',
                    color='pink'
                ).classes(
                    'text-base p-3'
                )

                ui.icon(
                    'arrow_forward',
                    color='grey'
                )

                ui.badge(
                    'Assessment',
                    color='orange'
                ).classes(
                    'text-base p-3'
                )

                ui.icon(
                    'arrow_forward',
                    color='grey'
                )

                ui.badge(
                    'Evaluation',
                    color='teal'
                ).classes(
                    'text-base p-3'
                )

        # -------------------------------------------------
        # DASHBOARD CARDS
        # -------------------------------------------------

        with ui.row().classes(
            'w-full justify-center gap-6 flex-wrap'
        ):

            # COURSE SETUP

            with ui.card().classes(
                'w-64 p-6 hover:shadow-xl'
            ).style(
                '''
                border-top: 6px solid #2563eb;
                border-radius: 18px;
                min-height: 275px;
                '''
            ):

                ui.icon(
                    'school',
                    size='48px',
                    color='blue'
                )

                ui.label(
                    'Course Setup'
                ).classes(
                    'text-xl font-bold'
                )

                ui.label(
                    'Create programmes, courses and academic information.'
                ).classes(
                    'text-gray-600'
                )

                ui.space()

                ui.button(
                    'Open Course Setup',
                    icon='arrow_forward',
                    on_click=lambda: ui.navigate.to('/course-setup')
                ).props(
                    'outline'
                )

            # PLO / CLO

            with ui.card().classes(
                'w-64 p-6 hover:shadow-xl'
            ).style(
                '''
                border-top: 6px solid #7c3aed;
                border-radius: 18px;
                min-height: 275px;
                '''
            ):

                ui.icon(
                    'account_tree',
                    size='48px',
                    color='purple'
                )

                ui.label(
                    'PLOs & CLOs'
                ).classes(
                    'text-xl font-bold'
                )

                ui.label(
                    'Define outcomes and create meaningful PLO-CLO alignment.'
                ).classes(
                    'text-gray-600'
                )

                ui.space()

                ui.button(
                    'Manage Outcomes',
                    icon='arrow_forward',
                    on_click=lambda: ui.navigate.to('/outcomes')
                ).props(
                    'outline'
                )

            # LESSON PLANNER

            with ui.card().classes(
                'w-64 p-6 hover:shadow-xl'
            ).style(
                '''
                border-top: 6px solid #ec4899;
                border-radius: 18px;
                min-height: 275px;
                '''
            ):

                ui.icon(
                    'edit_note',
                    size='48px',
                    color='pink'
                )

                ui.label(
                    'Lesson Planner'
                ).classes(
                    'text-xl font-bold'
                )

                ui.label(
                    'Design constructively aligned teaching, '
                    'learning and assessment.'
                ).classes(
                    'text-gray-600'
                )

                ui.space()

                ui.button(
                    'Create Lesson Plan',
                    icon='auto_awesome',
                    on_click=lambda: ui.navigate.to('/lesson-planner')
                ).props(
                    'unelevated'
                ).style(
                    '''
                    background-color: #ec4899;
                    color: white;
                    '''
                )

            # SAVED PLANS

            with ui.card().classes(
                'w-64 p-6 hover:shadow-xl'
            ).style(
                '''
                border-top: 6px solid #14b8a6;
                border-radius: 18px;
                min-height: 275px;
                '''
            ):

                ui.icon(
                    'folder_open',
                    size='48px',
                    color='teal'
                )

                ui.label(
                    'Saved Plans'
                ).classes(
                    'text-xl font-bold'
                )

                ui.label(
                    'Access and review previously created lesson plans.'
                ).classes(
                    'text-gray-600'
                )

                ui.space()

                ui.button(
                    'View Plans',
                    icon='arrow_forward',
                    on_click=lambda: ui.navigate.to('/saved-plans')
                ).props(
                    'outline'
                )

        # -------------------------------------------------
        # BOTTOM MESSAGE
        # -------------------------------------------------

        with ui.card().classes(
            'w-full p-7 text-center'
        ).style(
            '''
            background: linear-gradient(
                90deg,
                #eef2ff,
                #fdf2f8
            );
            border-radius: 20px;
            border: 1px solid #ede9fe;
            '''
        ):

            ui.icon(
                'lightbulb',
                size='40px',
                color='amber'
            )

            ui.label(
                'OBE is more than mapping outcomes.'
            ).classes(
                'text-2xl font-bold'
            )

            ui.label(
                'Effective lesson planning connects what students should achieve, '
                'what they do in class, how learning is assessed, and how teaching '
                'is continuously improved.'
            ).classes(
                'text-lg text-gray-700 max-w-4xl mx-auto'
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

       

        # =====================================================
        # OBE ALIGNMENT CHECK
        # =====================================================

        def check_alignment():

            missing_fields = []

            if not selected_course.value:
                missing_fields.append('Course')

            if not selected_clo.value:
                missing_fields.append('CLO')

            if not topic.value:
                missing_fields.append('Lesson Topic')

            if not lesson_outcome.value:
                missing_fields.append('Lesson Learning Outcome')

            if not teaching_method.value:
                missing_fields.append('Teaching Method')

            if not activity.value:
                missing_fields.append('Teaching / Learning Activity')

            if not assessment_method.value:
                missing_fields.append('Assessment Method')

            if not assessment_task.value:
                missing_fields.append('Assessment Task')

            if not success_criterion.value:
                missing_fields.append('Success Criterion')

            if not evaluation.value:
                missing_fields.append('Evaluation / Improvement Plan')

            if missing_fields:
                ui.notify(
                    'Please complete: ' + ', '.join(missing_fields),
                    type='warning',
                    timeout=6000
                )
                return

            # -------------------------------------------------
            # BASIC OBE ALIGNMENT SCORE
            # -------------------------------------------------

            score = 0
            feedback = []

            # CLO selected
            if selected_clo.value:
                score += 20
                feedback.append('✓ CLO selected and linked to the lesson.')

            # Lesson outcome
            if lesson_outcome.value:
                score += 20
                feedback.append('✓ Lesson learning outcome is defined.')

            # Teaching activity
            if activity.value and teaching_method.value:
                score += 20
                feedback.append(
                    '✓ Teaching method and learning activity are included.'
                )

            # Assessment
            if assessment_method.value and assessment_task.value:
                score += 20
                feedback.append(
                    '✓ Assessment method and task are specified.'
                )

            # Evaluation
            if success_criterion.value and evaluation.value:
                score += 20
                feedback.append(
                    '✓ Success criterion and improvement plan are included.'
                )

            # -------------------------------------------------
            # SHOW RESULT
            # -------------------------------------------------

            with ui.dialog() as dialog, ui.card().classes(
                'w-full max-w-2xl p-6'
            ):

                ui.label(
                    'OBE Alignment Check'
                ).classes(
                    'text-2xl font-bold'
                )

                if score >= 80:
                    ui.icon(
                        'check_circle',
                        color='green',
                        size='55px'
                    )

                    ui.label(
                        f'Alignment Score: {score}%'
                    ).classes(
                        'text-2xl font-bold text-green-700'
                    )

                    ui.label(
                        'This lesson demonstrates strong OBE alignment.'
                    ).classes(
                        'text-lg'
                    )

                elif score >= 60:
                    ui.icon(
                        'warning',
                        color='orange',
                        size='55px'
                    )

                    ui.label(
                        f'Alignment Score: {score}%'
                    ).classes(
                        'text-2xl font-bold text-orange-700'
                    )

                    ui.label(
                        'The lesson is partially aligned. '
                        'Some elements should be strengthened.'
                    )

                else:
                    ui.icon(
                        'error',
                        color='red',
                        size='55px'
                    )

                    ui.label(
                        f'Alignment Score: {score}%'
                    ).classes(
                        'text-2xl font-bold text-red-700'
                    )

                    ui.label(
                        'The lesson requires further OBE alignment.'
                    )

                ui.separator()

                ui.label(
                    'Alignment Evidence'
                ).classes(
                    'text-xl font-semibold'
                )

                for item in feedback:
                    ui.label(item)

                ui.button(
                    'Close',
                    on_click=dialog.close
                ).props('outline')

            dialog.open()


        # =====================================================
        # SAVE LESSON PLAN
        # =====================================================

        def save_lesson_plan():

            if not selected_course.value:
                ui.notify(
                    'Please select a course first.',
                    type='negative'
                )
                return

            if not selected_clo.value:
                ui.notify(
                    'Please select a CLO first.',
                    type='negative'
                )
                return

            if not topic.value:
                ui.notify(
                    'Please enter the lesson topic.',
                    type='negative'
                )
                return

            ui.notify(
                'Lesson plan is complete. '
                'Database storage will be connected next.',
                type='positive',
                timeout=5000
            )


        # =====================================================
        # BUTTONS
        # =====================================================

        with ui.row().classes(
            'gap-4 q-mt-md'
        ):

            ui.button(
                'Check OBE Alignment',
                icon='fact_check',
                on_click=check_alignment
            ).props(
                'unelevated'
            )

            ui.button(
                'Save Lesson Plan',
                icon='save',
                on_click=save_lesson_plan
            ).props(
                'unelevated'
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
