template1 = '''
The Employment Strategy for %(firstname)s %(lastname)s has been reviewed.  At the conclusion of the strategy review, %(gen)s %(lastname)s was referred to skills development for additional job seeker services as warranted.
<br><br>
An orientation was given that provided an overview of the Re-Employment process and expectations for a successful compliance. Staff also provided information outlining the following relevant Career Center services:<br>
-Access to computers and office machines<br>
-Assessments for skills and interests<br>
-Website navigation<br>
-Other online tools to aid in job search<br>
-Labor Market Information<br>
-Grant funded Training<br>

An assessment of %(gen)s %(poss)s background, which included information about %(gen1)s education, work history, occupational desires, skill sets, strengths, and any identifiable barriers to employment was conducted.  Using the assessed information along with current labor market information, staff developed an individualized plan to aid %(gen)s %(lastname)s in finding employment.
<br><br>
At the conclusion of the visit, a virtual recruiter was established using the current desired occupation and instructions on creating additional virtual recruiters was also discussed.

<br>
'''

template2 = '''
        %(firstname)s %(lastname)s completed the first RESEA service point.  Staff provided an overview of available career center services and on the intent and purpose of the Re-Employment program. Staff briefed %(gen)s %(lastname)s on how to successfully complete each service point of the re-employment process and provided labor market information that would best serve in conducting more efficient job searches. 
<br>
        A comprehensive assessment was then conducted, which provided gainful insight into  %(gen)s %(poss)s background, education, work history, strengths, and any identifiable barriers. Absent any sudden and significant changes, an individualized course of action was created to aid  %(gen)s %(lastname)s job search. A virtual recruiter was also established using the current desired occupation.
<br><br>
        At the conclusion of The Employment Strategy review, %(gen)s %(lastname)s was referred to skills development for additional job seeker services as warranted. 


        '''

template3 = '''
        (1) Conducted an orientation and explained the various benefits of using the career center for job search. <br>
        (2) Reviewed the key required components for successful completion of the RESEA program.<br>
        (3) Also reviewed the Employment Strategy for and referred the participant to skills development for additional job seeker services.<br>
        (4) Performed an assessment of %(firstname)s %(poss)s background which was then used in conjunction with current labor market information to craft an individualized employment plan.<br>
        (5) virtual recruiter was also established using the current desired occupation to generate more job leads.
<br><br>
        '''

template4 = '''
        The Employment Strategy review session was conducted for %(firstname)s %(lastname)s.  During the course of the review, instructions on expectations and succesful completion of the program was disseminated.   %(lastname)s has been referred to skills development for additional job seeker services as warranted. <br><br>

        Revealed information on locating labor market information and setting up virtual recruiters for job openings notifications.<br><br>

        Conducted comprehensive assessment revealed information about %(gen)s %(poss)s background, work history, skill sets, strengths, and any identifiable barriers. <br><br>

        In conjuction with the participant, staff was able to craft a short term individualized plan to assist %(gen)s %(lastname)s in obtaining employment.

        '''

template5 = '''
        After a review of the employment strategy plan, %(gen)s  %(lastname)s was referred to skills development for additional job seeker services.
        The orientation session provided an overview of the Re-Employment process and expectations for successful compliance.  Information about other accessible career center services was also provided.
        A virtual recruiter was established using the current desired occupation and instructions on creating additional virtual recruiters was also discussed.

        An assessment of %(gen)s %(poss)s skills/background was used to craft an individualized employment plan.
<br>
        '''


template6 =  '''
        Orientation regarding career center services, discussion on most recent employment history, and future career expectations for %(firstname)s %(lastname)s has been completed in this strategy review session.
        A comprehensive assessment was also conducted to aid in the development of an Individualized Employment Plan.
        At the conclusion of this review, %(gen)s %(poss)s was referred to skills development for assistance on crafting a virtual recruiter and for any other as needed job seeker services.

        '''


template7 = '''
        %(gen)s %(firstname)s %(lastname)s completed SP1 of the RESEA program.
        A one on one orientation conducted gave the participant an outline on program requirements and future obligations required for satisfactory compliance. 
        A virtual recruiter was created after a brief discussion about current labor market info and employment expectations.
        Further staff assisted services were offered as warranted. 
        Distinguishing and notable information identified through the initial and comprehensive assessments follow below: 
<br>        
                             '''
doom1 = '''
        The following is a brief background/summary
            %(firstname)s %(lastname)s most recently worked at %(company)s in the %(industry)s industry and has %(years)s years of experience  %(indef)s %(job_title)s. 
            %(gen)s %(lastname)s most recently earned $%(hour_wage)s/hr and  %(gen2)s  %(wag)s.
            %(gen)s  %(lastname)s %(sent)s 
            %(comments)s <br>
        '''
doom2 = '''
<br>
        -Summary:<br>
            %(gen)s %(lastname)s %(sent)s <br>
            %(firstname)s %(lastname)s worked at %(company)s in the %(industry)s industry <br>
            %(gen)s %(lastname)s   has %(years)s years of experience %(indef)s %(job_title)s
            and most recently earned $ %(hour_wage)s/hr. <br>
            %(gen2)s %(wag)s .<br>
            %(comments)s
            <br>
        '''
doom3 = '''
<br>
        -Summary:- <br>
            %(gen2)s worked at %(company)s in the %(industry)s industry and most recently earned $%(hour_wage)s/hr.<br>
            %(firstname)s %(lastname)s has worked  %(indef)s %(job_title)s for %(years)s years. <br>
            %(gen)s %(lastname)s %(sent)s <br>
            %(comments)s
            <br><br>
        '''

doom4 = '''
            %(gen2)s worked at %(company)s in the %(industry)s industry and most recently earned $%(hour_wage)s/hr. %(firstname)s %(lastname)s has worked  %(indef)s %(job_title)s  for %(years)s  years. %(gen)s  %(lastname)s %(sent)s.
        '''

boom1 = '''
<br>
        -Assessment:- <br>
            %(gen2)s would like to work a full time schedule. <br>
             %(zipc)s <br>
             <br>
             *Strengths, Barriers, and Job Readiness*: <br>
             %(bars)s 
             %(stren)s
    

             Based on recent employment history and these findings, %(firstname)s %(lastname)s is work ready. %(gen)s %(lastname)s has been advised to continue in current job search efforts.<br>
             %(refs)s
             <br><br>
        '''
boom2 = '''
             %(gen)s %(lastname)s prefers a full time schedule. <br>
             %(zipc)s <br><br>

             The indications from the comprehensive assessment are as follows: <br>
             • %(bars)s
             • %(stren)s <br>

             Based on these findings, %(firstname)s %(lastname)s is work ready.  %(gen)s %(lastname)s has been advised to focus on desired employment goals at this stage of the job search. <br>
             %(refs)s <br>
        '''

boom3 = '''
        Findings from assessment and strategy review: <br>
             %(zipc)s <br>
             The comprehensive results revealed the following: <br>
             • %(stren)s
             • %(bars)s <br><br>
             These findings suggest that %(firstname)s %(lastname)s is work ready.  %(gen2)s has been encouraged
             to maintain current job search efforts.<br>
             %(refs)s <br>
             <br>
        '''

boom4 = '''
             %(zipc)s <br>. %(stren)s <br>  %(bars)s <br>
             %(firstname)s %(lastname)s is work ready and has been encouraged to utilize career center in %(gen1)s job search. <br>
             %(refs)s <br>
        '''