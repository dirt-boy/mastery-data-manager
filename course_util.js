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

function getRoster(response) {
  return {}
}

function formatAll(response) {
    return {
      courses: getCourseList(response, 'courses'),
      courseWork: getCourseList(response, 'courseWork'),
      roster: getRoster(response)
    }
}
