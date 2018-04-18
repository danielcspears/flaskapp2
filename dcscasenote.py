from flask import  Flask, Blueprint,  render_template, request, session
import random
from srttemp import template1, template2, template3, template4, template5, template6, template7, boom1, boom2, boom3, boom4, doom1, doom2, doom3, doom4

case_note_blueprint = Blueprint('case_note', __name__)
@case_note_blueprint.route('/casenote', methods = ['POST','GET'])   
def case_note():
    casenote = {}
    if request.method == 'POST':
        casenote['firstname'] = request.form['firstname'].capitalize()
        casenote['lastname'] = request.form['lastname'].capitalize()
        casenote['job_title'] = request.form['job_title']
        casenote['des_title'] = request.form['des_title']
        casenote['gender'] = request.form['gender'].lower()
        casenote['company'] = request.form['company'].capitalize()
        casenote["industry"] =  request.form['industry'].lower()
        casenote['years'] = int(request.form['years'])
        casenote["hour_wage"] = float(request.form['hour_wage'])
        casenote["exp_wage"] = float( request.form['exp_wage'])
        casenote["referrals"] = request.form['referrals'].casefold()
        casenote["strengths"] = request.form.getlist('strength')
        casenote["strengths"] = str(", ".join(casenote["strengths"]))
        casenote["barriers"] = request.form.getlist('barrier')
        casenote["barriers"] = str(", ".join(casenote['barriers']))
        casenote["comments"] = request.form['comments'].capitalize()
        casenote["zip"] = int(request.form['zipcode'])
        casenote["relocate"] = request.form.getlist('willing')
        casenote["relocate"] = str("".join(casenote["relocate"]))
        
        if casenote['lastname'].endswith(('s')):
            casenote['poss'] = casenote['lastname'] +"'"
        elif casenote['lastname'].endswith(('z')):
            casenote['poss'] = casenote['lastname'] +"'"
        else:
            casenote['poss'] = casenote['lastname'] +"'s"

        if casenote['gender'] == "male":
            casenote['gen'] = "Mr. " 
        else:   
            casenote['gen'] = "Ms. " 

        if casenote['gender'] == "male":
            casenote['gen1'] = "his "
        else:   
            casenote['gen1'] = "her "

        if casenote['gender'] == "male":
            casenote['gen2'] = "He "
        else:   
            casenote['gen2'] = "She "


        if casenote['job_title'].endswith(('^[aeiou].*')):
            casenote['indef'] = " as an "
        else:
            casenote['indef'] = " as a "


        if casenote['des_title'].endswith(('^[aeiou].*')):
            casenote['indef'] = " as an "
        else:
            casenote['indef'] = " as a "    


        if casenote['job_title'] == casenote['des_title']:
            casenote['sent'] = "will continue looking for work" + casenote['indef'] + casenote['des_title']
        else:
            casenote['sent'] = "is looking to transition to another occupation "


        if casenote['hour_wage'] == casenote['exp_wage']:
            casenote['wag'] = "has expectations of earning around the same wage."
        elif casenote['hour_wage'] < casenote['exp_wage']:
            casenote['wag'] = "has expectations of earning a higher wage."
        else:
            casenote['wag'] =  "would like to retain a strategic open/negotiable position regarding future salary expectations.  "


        if  not casenote['referrals']:
            casenote['refs'] = "No referrals were made at this service point."
        else:
            casenote['refs'] = "A job referral was made to:  " + casenote['referrals']


        if not casenote['barriers']:
            casenote['bars'] = "No barriers were identified in this assessment.<br>"
        else:
            casenote['bars'] = "The following barriers were identified during the course of this assessment: " + casenote['barriers']+".<br>"

        if not casenote['strengths']:
            casenote['stren'] = "Easily identifiable strengths proved elusive in this discovery process.<br>"
        else:
            casenote['stren']="The following strengths were identified during the course of this assessment: " + casenote['strengths']                     +".<br>"

        if casenote['relocate'] == 'yes':
            casenote['zipc'] = casenote['gen2'] + " is willing to relocate for the right position but would prefer opportunities within a                 25 mile radius of " + str(casenote['zip']) +"."
        else:
            casenote['zipc']= casenote['gen2'] + " is not willing to relocate and is searching for job opportunities within a 25 mile                     radius of " + str(casenote['zip']) +"."


        x = random.randint(1,21)
        y = random.randint(1,4)
        z = random.randint(1,4)

        if y == 1:
            doome = doom1
        elif y == 2:
            doome = doom2
        elif y == 3:
            doome = doom3
        else:
            doome = doom4

        if z == 1:
            boome = boom1
        elif z == 2:
            boome = boom2
        elif z== 3:
            boome = boom3
        else:
            boome = boom4

        if x <= 3:
            lettuce = ((template1 % casenote) +(doome % casenote)+ (boome % casenote))
        elif x <= 6 & x >= 4:
            lettuce = ((template2 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 9 & x >= 7:
            lettuce = ((template3 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 12 & x >= 10:
            lettuce = ((template4 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 15 & x >= 13:
            lettuce = ((template5 % casenote)+(doome % casenote)+ (boome % casenote))
        elif x <= 18 & x >= 16:
            lettuce = ((template6 % casenote)+(doome % casenote)+ (boome % casenote))
        else:
            lettuce = ((template7 % casenote)+(doome % casenote)+ (boome % casenote))
            
        return render_template("makenote.html", casenote=casenote, lettuce = lettuce)