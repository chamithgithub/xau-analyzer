📅 Step 2: Use Task Scheduler
Press Win + S → Search: Task Scheduler → Open it

On the right → click Create Basic Task

Name it: Run XAU/USD Bot

Trigger: Daily

Start time: e.g., 08:00 AM

Repeat task every:

Click "Open Advanced Properties"

In the Triggers tab → Edit

Check Repeat task every 15 minutes

Duration: 1 day

Action: Start a Program

Program/script:
cmd.exe

Add arguments:

txt
Copy
Edit
/c "E:\pactrice\python\xau-analyzer\run_main.bat"
Finish ✔️

# # web site
cd E:\pactrice\python\xau-analyzer
python web/app.py


## run

python main.py


## requirements.txt install


### 'newsapi', 'gnews', or 'fxstreet'