function getCourseList(courseData, prop) {
    var titles = {}
    for (var i = 0; i <= courseData.length; i++) {
        if (typeof courseData[i] === 'object' && courseData[i][prop]) {
            for (var j = 0; j <= courseData[i][prop].length; j++) {
                if (courseData[i][prop][j]) {
                    titles[courseData[i][prop][j].id] = courseData[i][prop][j].title || courseData[i][prop][j].name
                }
            }
        }
    }
    return titles
  }

function getRoster(resp) {
  var roster = {
    teachers: {},
    students: {}
  }
  for (var i = 0; i<= resp.length; i++) {
    if(typeof resp[i] === 'object' && (resp[i].teachers || resp[i].students)) {
      if (resp[i].teachers) {
        for (var j = 0; j <= resp[i].teachers.length; j++) {
          if (resp[i].teachers[j]) {
            roster.teachers[resp[i].teachers[j].userId] = resp[i].teachers[j].profile.name.fullName
          }
        }
      }
      if (resp[i].students) {
        for (var j = 0; j <= resp[i].students.length; j++) {
          if (resp[i].students[j]) {
            roster.students[resp[i].students[j].userId] = resp[i].students[j].profile.name.fullName
          }
        }
      }
    }
  }
  return roster
}

function rosterByCourse(resp) {
  var roster = {
  }
  for (var i = 0; i<= resp.length; i++) {
    if (typeof resp[i] === 'object' && (resp[i].teachers || resp[i].students)) {
      if (resp[i].teachers) {
        for (var j = 0; j <= resp[i].teachers.length; j++) {
          if (resp[i].teachers[j] && resp[i].teachers[j].courseId && resp[i].teachers[j].userId) {
            if (roster[resp[i].teachers[j].courseId]) {
              roster[resp[i].teachers[j].courseId].teachers[resp[i].teachers[j].userId] = resp[i].teachers[j]
            }
            if (!roster[resp[i].teachers[j].courseId]) {
              roster[resp[i].teachers[j].courseId] = {
                teachers: {},
                students: {}
              }
              roster[resp[i].teachers[j].courseId].teachers[resp[i].teachers[j].userId] = resp[i].teachers[j]
            }
          }
        }
      }
      if (resp[i].students) {
        for (var j = 0; j <= resp[i].students.length; j++) {
          if (resp[i].students[j] && resp[i].students[j].courseId && resp[i].students[j].userId) {
            if (roster[resp[i].students[j].courseId]) {
              roster[resp[i].students[j].courseId].students[resp[i].students[j].userId] = resp[i].students[j]
            }
            if (!roster[resp[i].students[j].courseId]) {
              roster[resp[i].students[j].courseId] = {
                teachers: {},
                students: {}
              }
              roster[resp[i].students[j].courseId].students[resp[i].students[j].userId] = resp[i].students[j]
            }
          }
        }
      }
    }
  }
  return roster
}

function formatAll(response) {
    return {
      courses: getCourseList(response, 'courses'),
      courseWork: getCourseList(response, 'courseWork'),
      roster: getRoster(response),
      rosterByCourse: rosterByCourse(response)
    }
}
