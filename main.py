from pyodide.ffi import create_proxy 
from js import document
from pyscript import display

# -------------------------------------
# SIGN UP PAGE
# -------------------------------------
def signupbtn(event): 
    output = document.getElementById('output')
    username = document.getElementById('username').value
    output.innerHTML = ""
    usernamelens = len(username)

    p = document.getElementById('password').value
    findingp = p.isdigit() #returns as false if password has all letters only
    findingp2 = p.isalpha() #returns as fale if password has all numbers only
    findingp3 = p.isalnum()

    if usernamelens < 7: 
        output.innerText = "Sorry! Try again with a username that has more than 7 characters."
        return 

    if findingp == False and findingp2 == True: 
        output.innerText = "ERROR: Your password must contain at least 1 numerical digit."
    elif findingp == True and findingp2 == False: 
        output.innerText = "ERROR: Your password must contain at least 1 letter."
    elif findingp3 == True: 
        output.innerText = "Password and account created!"

# --------------------------------------

# ------------------------------
# TEAM DATA: Mapping grade-section combinations to Intramurals teams
# ------------------------------
# The key is "Grade-SECTION" in uppercase to match the dropdown input.
# The value is the team assigned to that combination.
team_data = {
    "7-RUBY": "Yellow Tigers",
    "8-EMERALD": "Yellow Tigers",
    "9-SAPPHIRE": "Yellow Tigers",
    "10-SAPPHIRE": "Yellow Tigers",
    "11-LUNA": "Yellow Tigers",

    "7-SAPPHIRE": "Green Hornets",
    "8-RUBY": "Green Hornets",
    "9-TOPAZ": "Green Hornets",
    "10-EMERALD": "Green Hornets",
    "12-TINIO": "Green Hornets",

    "7-EMERALD": "Blue Bears",
    "8-TOPAZ": "Blue Bears",
    "8-JADE": "Blue Bears",
    "9-RUBY": "Blue Bears",
    "10-TOPAZ": "Blue Bears",
    "12-JOSE": "Blue Bears",

    "7-TOPAZ": "Green Hornets",
    "8-SAPPHIRE": "Green Hornets",
    "9-JADE": "Green Hornets",
    "9-EMERALD": "Green Hornets",
    "10-RUBY": "Green Hornets",
    "11-AMORSOLO": "Green Hornets",
}

# ------------------------------
# TEAM BANNERS: Mapping team names to their banner images
# ------------------------------
# The key is the team name, the value is the URL of the banner image
team_banners = {
    "Yellow Tigers": "YELLOW.png",
    "Green Hornets": "GREEN.png",
    "Red Bulldogs": "RED.png",
    "Blue Bears": "BLUE.png",
}

# ------------------------------
# FUNCTION: check_eligibility
# This function is called when the user clicks the "Check Eligibility" button
# ------------------------------
def check_eligibility(event):
    """
    Determines if a student is eligible for Intramurals based on registration,
    medical clearance, grade, and section. Uses nested if/elif/else statements.
    """

    # Grab the div where results will be displayed
    result_div = document.getElementById("result")
    result_div.innerHTML = ""  # Clear previous messages to avoid stacking results

    # ------------------------------
    # Check registration
    # ------------------------------
    reg = document.querySelector('input[name="registration"]:checked')  # Grab selected radio
    if not reg:  # If nothing selected
        result_div.innerHTML = "<p style='color:#d4a373;'>Please select registration.</p>"
    else:
        if reg.value != "Yes":  # If registration is "No"
            result_div.innerHTML = "<p style='color:#d4a373;'>You need to register online.</p>"
        else:
            # ------------------------------
            # Check medical clearance
            # ------------------------------
            med = document.querySelector('input[name="medical"]:checked')
            if not med:  # If nothing selected
                result_div.innerHTML = "<p style='color:#d4a373;'>Please select medical clearance.</p>"
            else:
                if med.value != "Yes":  # If medical clearance is "No"
                    result_div.innerHTML = "<p style='color:#d4a373;'>You need to secure a medical clearance.</p>"
                else:
                    # ------------------------------
                    # Check grade and section
                    # ------------------------------
                    grade = document.getElementById("grade").value.strip()  # Remove spaces
                    section = document.getElementById("section").value.strip()

                    if grade == "" or section == "":  # If user left either empty
                        result_div.innerHTML = "<p style='color:#d4a373;'>Please select grade and section.</p>"
                    else:
                        key = f"{grade}-{section}".upper()  # Format key to match dictionary

                        # ------------------------------
                        # Nested conditional: eligible or not
                        # ------------------------------
                        if key in team_data:  # If combination exists
                            team = team_data[key]  # Get team name
                            banner_url = team_banners.get(team, "")  # Get banner URL

                            # Display eligibility message with team and banner
                            result_div.innerHTML = f"""
                                <h2 style='color:#f5f0e1;'>Congratulations! You are eligible!</h2>
                                <h2 class='mt-3'>{team}</h2>
                                <img src='{banner_url}' class='team-banner' alt='{team} Banner'>
                            """
                        else:  # Not eligible
                            result_div.innerHTML = "<p style='color:#d4a373;'>Sorry, you’re not eligible.</p>"

# ------------------------------
# BUTTON EVENT BINDING
# ------------------------------
btn = document.getElementById("checkBtn")

if btn is not None: #to ensure that the btn used in index 2 doesn't affect any other piece of code 
    btn_proxy = create_proxy(check_eligibility)
    btn.addEventListener("click", btn_proxy) 

# -------------------------------
# LIST OF PLAYERS 
# -------------------------------
def show_players(event):
    players = [ #list of players
        "Balagat, Michael",
        "Bernardo, Miko",
        "Caguiron, Carriena",
        "Calida, Lorenzo",
        "Chan, Jazmar",
        "Cruz, Rohann",
        "David, Antonio",
        "De Guzman, Uno",
        "De Guzman, Nia",
        "Francisco, Annika",
        "Kaur, Navjot",
        "Laconsay, Heleina",
        "Lepasana, Khen",
        "Lopez, Liam",
        "Lucman, Mohammad",
        "Malapitan, Caleb",
        "Manahan, Samantha",
        "Manuel, Elyze",
        "Mendoza, Matthew",
        "Palafox, Coby",
        "Ramirez, Alfiona",
        "Reynoso, Izeck",
        "Santos, Cas",
        "Santos, Rafaela",
        "Tolentino, Kelsey",
        "Toribio, Sasha",
        "Valdez, David"
    ]

    player_list = document.getElementById("players")
    player_list.innerHTML = "" #no repeats 

    for name in players: #used "for" loop in order to make the list of players
        li = document.createElement("li")
        li.innerText = name
        player_list.appendChild(li) #this one inserts the list item into the webpage

# -------------------------------