# Creating a Facebook App

## Create the App

I followed this guide.

[Automatically publish to facebook pages with python](https://blog.theodo.com/2019/02/automatically-publish-facebook-pages-python/)

#### Platform

At the very bottom of `Settings > Basic` you have to choose a platform. I chose website, and linked to the public github repository where my app is stored. If you don't have a public script, link to your business website.  In my case I bought a domain for my business, as mentioned below in [Business Verification](#business-verification)

#### Permissions Required

* `pages_read_engagement`
* `pages_manage_posts`

## App Review

Information required for completing app review should be found here:

[Server-to-Server Apps](https://developers.facebook.com/docs/apps/server-to-server-apps) 
> If your app has no user interface because it exchanges data directly with our APIs, refer to this guide when configuring your app's Basic Settings, and when completing App Review.

[Server-to-Server App Sample Submission](https://developers.facebook.com/docs/app-review/resources/sample-submissions/server-to-server)

[Common mistakes submitting for app review](https://developers.facebook.com/docs/app-review/submission-guide/common-mistakes)

## Business Verification

Facebook has suspended individual verification because of COVID. Business verification is required. That said, it appears my facebook posts are live now that my app has its app review, even without verification. I am checking by looking at the page in a browser not logged into FB. I will complete verification, but not sure I really need it for this app.

The following steps are obviously only for the USA. It will be required to create a business to publish a facebook app, until they bring back individual verification.

### Sole Proprietorship

Simplest cheapest way to register a business, can change this later if necessary.

[50 State Guide to Establishing a Sole Proprietorship](https://www.nolo.com/legal-encyclopedia/50-state-guide-establishing-sole-proprietorship.html)

for my state, this will cost only $40.

### EIN (optional)

Also useful will be to apply for EIN. This way you can open a bank account under the business name.

[Apply for an Employer Identification Number (EIN) Online](https://www.irs.gov/businesses/small-businesses-self-employed/apply-for-an-employer-identification-number-ein-online)

## Privacy Policy

This app does not collect or store any user data.

[Privacy Policy for MBR Quote Bot](Marshall-Rosenberg-Quotes/privacy.md)