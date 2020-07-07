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

UPDATE 2020.6.24

Just did a ton of cleanup! hope this keeps things nice and secure. Also many important gains were made today in the realm of rubric-reading. I am very excited to continue this work tomorroy


UPDATE 2020.7.07

ok so it works with headless chrome now which is nice. Its also capable of using regex to locate rubric data. Also nice. Unfortunately I am having difficulty packing the read rubric data into a log-worthy format. putting it into a python dict seems to be more trouble than it's worth. I am wondering if it would make more sense to simply... construct it in a more manual fashion. by which I mean iterating on the length of each regex list result and just adding in each piece within each for loop. Now that im writing it down that does seem like the simplest solution possible. I'll probably try that later. 

Currently I am trying to make things more modular by allowing the script to identify the dictionary of rubric keys (mutable), and then iterate through them to populate a dictionary. It doesn't sound too complicated but it turns out that, unfortunately, the raw html of each rubric contains duplicates of some of the keys. i.e. each criteria appears twice. like literally twice. 

For modularity purposes it would make sense to create a simple python dict out of these, avoiding any kind of number-specific iterables for deletion of repeats -- in the end, we really only need one of each key-value pair. Yeah. that makes sense. 

I think it makes sense to begin by drawing out a simple hierarchy of the dictionary structure I want. Like physically drawn. Typing it up appears to not work for me for some reason. But anyhoo. I will be trying to simplify this tomorrow morning so that I can complete the rubric pulling process. 

I fvcking hate these goddamn rubrics. difficult difficult lemon difficult.

ok bye.

-dirt-boy 2020.7.07
