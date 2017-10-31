import requests
import json
from json_data import jsonObj
from app import courseId, authToken

modules = jsonObj['Modules']
sections = jsonObj['Sections']
submodules = jsonObj['Submodules']
tracks = jsonObj['Tracks']
moduleArr = {'1': 'ce92724a-4da9-4a21-82c5-c052d35d7bbc', '3': 'a530286d-6822-460f-9a40-c5985d6deb41', '2': '3e01d138-9f08-4f13-a8c8-1b8ec737a7ce', '4': '85bdb235-4469-484c-aea7-15052b63c10b'}

def createSection(section, moduleIncrement, moduleId):
    url = "http://localhost:8080/v2/entity/section/" + moduleId
    headers = {
        "Content-Type": "application/json",
        "Authorization": authToken
    }

    params = {
        "name": section['Name'],
        "courseId": courseId,
        "order": section['Order']
    }

    response = requests.post(url, json=params, headers=headers)
    json_s = json.loads(response.text)
    return (json_s['data']['id'])

sectionIncreament = 1
sectionArr = {}
for sectionId in sections:
    section = sections[sectionId]
    moduleId = moduleArr[str(section['Module Id'])]
    sectionObjId = createSection(section, sectionIncreament, moduleId)
    sectionArr[str(section['Section id'])] = {"module": moduleId, "section": sectionObjId}
    sectionIncreament = sectionIncreament + 1

print(sectionArr)