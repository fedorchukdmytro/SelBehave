Feature: Testing Zombie site
Scenario: Testing homepage
  Given a Zombie site
  Then open home page
  Then test element blog
  Then test element brains
  Then test element home
  Then test element more
  Then test element regular
  Then test element lite
  Then close window
  
  