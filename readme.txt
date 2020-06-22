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

-dirt-boy, 2020.6.221
