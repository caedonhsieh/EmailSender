# EmailSender

The email sender application uses SMTP to send emails to and from specified addresses. Yes, this means you can use it to send spoof emails. No, this does not mean you should abuse this for malicious purposes. Please use responsibly.

## Instructions for setup

1. Clone this repository.
2. Navigate to the project root in a terminal window.
3. Run the command `./setup.sh`.

## Instructions for use

There are two interfaces for this project: a webpage interface and a CLI interface.

#### Webpage interface

1. Run the command `./launcher.py'
2. Open your favorite web browser and navigate to `localhost:8000`.
3. Input text into the input fields, then click "Submit".

#### CLI interface

1. Run the command `./send_email.py`
2. Follow the prompts.

#### Other notes

* The default domain used is google.com.
* Certain email addresses will not work.
