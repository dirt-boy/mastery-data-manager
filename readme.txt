Hello friends.

I am creating this document to ensure there is a reasonable history of the development of this application.

This app is intended to pull data from Google Classroom, send it to an instance of the ELK stack in Google Cloud hosted in a neat Kubernetes cluster, and then push that data into a Salesforce instance at the command of a sysadmin. 

Currently this project is going very smoothly, minus difficulties in accessing google classroom rubric data. I have struggled greatly with this issue for what feels like eons. At this point I am attempting to spoof a google login in order to collect the necessary login cookies to perform an HTTP POST request for rubric data in JSON format.

Currently this seems to be the best option.

There are 2 existing issues:
  1. Running headless Chrome seems to null the driver's ability to load web elements. I am reasonably sure I can find a workaround to this, but if push comes to shove we can use a different browser that has less strict security, specifically relating to automated processes. Perhaps Firefox.
  2. I am still working out how to format the cookies saved from the Chrome webdriver such that they are accepted by Google's OAuth2 flow. It appears that if the correct cookies are provided, an OAuth2 token is not necessary for authentication. I find this very interesting.

  But aside from the intrigue this poses, I have determined that are two cookies necessary for a successfully google login:
  	
	__Secure-3PSID
	CONSENT
	SEARCH_SAMESITE
	SID
  
  These tokens all pertain to a user's login history and identity (as a google user). None of Google's advertising cookies are necessary to complete a login, though proceeding this way may cause heightened security-- such as calling for additional user/password information, etc. This is simply because Google additionally uses their peripheral advertising cookies to manage security. Again, this is very interesting. But that is beyond the point of this document.

I figure that by documenting this thought process I may at least be able to pick up where I left off. And please don't forget to remove the hellishly unnecessary .vimrc edits made previously. They are truly horrendous.

Ok. Thanks. Bye.

-dirt-boy, 2020.6.21

UPDATE 2020.6.22

I have abandoned hope of completing a proper Python Requests implementation for pulling rubric datya. 

Time is of the essence.

I have instead switched to saving full copies of the html of a rubric page, which can then be used to harvest the rubric data (as far as I have explored -- which is likely farther than most who don't regularly work on Google Classroom -- html class tags for elements are consistent throughout different rubrics. I have yet to experiment with class tags across classrooms or users, but I will have to wait until I have access to additional test data to look into this.

As such, I will be focusing on constructing JSON objects out of the raw page html. In hindsight, this may actually imply less effort and data formatting than the precious Requests library method.

We shall see. 

For the time being this will be my course of action.

As the goal of this project is to have a minimum viable product completed by the end of June 2020, I will save tinkering with http requests for the polishing phase.

Thanks for rading these logs.

-dirt-boy, 2020.6.22

UPDATE 2020.6.23

rubric_reader.py now allows the application to write a single slice of html content to a new file -- in essence this is isolating just the rubric data for us to parse. The next step, I believe, is constructing a functional dictionary of html class tags that indicate different parts of each rubric. This may require some discussion with Michael and Alyxe to ensure that rubrics will not extend beyond a certain number of gradeable items, i.e. i do not have to prepare a dictionary that is flexible enough to accomodate an infinite number of entries.

My hope is that this will take a minimal amount time, and I will be able to move onto appending the rubric data to the final product produced and logges by course_util.

Thanks for coming to my ted talk.
bye

-dirt-boy 2020.6.23


