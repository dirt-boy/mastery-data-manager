function getCourseList(courseData) {
    var titles = {}
    for (var i = 0; i <= courseData.length; i++) {
        if (typeof courseData[i] === 'object' && courseData[i]['courseWork']) {
            for (var j = 0; j <= courseData[i]['courseWork'].length; j++) {
                if (courseData[i]['courseWork'][j]) {
                    titles[courseData[i]['courseWork'][j].id] = courseData[i]['courseWork'][j].title
                }
            }
        }
    }
    return titles
  }
