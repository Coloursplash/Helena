import skills.greetings as greetings
import skills.quitting as quitting
import skills.helena as helena
import skills.time as time
import skills.activity as activity


def get_skills():
    skills = []
    skills.append(greetings.skill)
    skills.append(quitting.skill)
    skills.append(helena.skill)
    skills.append(time.skill)
    skills.append(activity.skill)
    return skills
