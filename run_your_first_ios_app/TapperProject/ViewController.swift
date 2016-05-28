//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit
import Social

class ViewController: UIViewController {
    
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var label_taps: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    @IBOutlet weak var high_score_label: UILabel!
    @IBOutlet weak var twitter_share: UIButton!
    
    //variables for taps
    var taps_done:Int = 0
    var taps_requested:Int = 0
    
    //variables for timer
    var timer = NSTimer()
    var time_passed:Float = 0
    var high_score:Float = 999999 //an arbitary huge number
    
    //output filename and old score from output file variable
    let filename = "best_taps_score.txt"
    var old_score:Float = 999999   //an arbitary huge number
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib
        readOldScore()
        updateHighScoreLabel()
        //print("\(old_score) is the old score")
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    //action for play button press
    @IBAction func clickPlayButton(sender: AnyObject) {
        if let taps = Int(self.textfield_number!.text!){
            if taps>0{
                print("Let's do \(taps) taps")
                self.taps_requested = taps
                initGame()
            }
        }
    }
    
    //action for clicking the coin button
    @IBAction func clickCoinButton(sender: AnyObject) {
        checkScore()
        print("Tap!")
        self.taps_done+=1
        updateTapCounter()
        if self.taps_done >= self.taps_requested{
            resetGame()
        }
    }
    
    //initialize game begin
    func initGame(){
        //hide these
        self.image_tapper.hidden = true
        self.button_play.hidden = true
        self.textfield_number.hidden = true
        self.high_score_label.hidden = true
        self.twitter_share.hidden = true
        //show these
        self.label_taps.hidden = false
        self.button_coin.hidden = false
        //initialize these variables
        self.taps_done = 0
        updateTapCounter()
        //timer - every 0.1 seconds, this timer will add 0.1 to time_passed
        self.timer = NSTimer.scheduledTimerWithTimeInterval(0.1, target: self, selector: #selector(countUp), userInfo: nil, repeats: true)
    }
    
    //connected with NSTimer, adds 0.1 to time_passed after every 0.1s
    func countUp(){
        self.time_passed+=0.1
        time_passed = Float(round(10*time_passed)/10)
        //preventive measure, so that timer doesn't keep on iterating
        if self.time_passed >= 999999 {
            resetGame()
        }
        //print("\(self.time_passed) is time passed")
    }
    
    //checks if current high score is greater than the previous current high score
    func checkScore(){
        if self.high_score > self.time_passed{
            self.high_score=self.time_passed
        }
        self.time_passed=0
    }
    
    //updates number of taps label
    func updateTapCounter(){
        self.label_taps.text = "\(taps_done) Taps"
    }
    
    //reset game function
    func resetGame(){
        //show these
        self.image_tapper.hidden = false
        self.button_play.hidden = false
        self.textfield_number.hidden = false
        self.high_score_label.hidden = false
        self.twitter_share.hidden = false
        //hide these
        self.label_taps.hidden = true
        self.button_coin.hidden = true
        //reset these variables
        self.taps_requested = 0
        self.textfield_number.text = ""
        //invalidate and reset timer
        self.timer.invalidate()
        //print("\(high_score) is high score")
        self.time_passed=0
        self.timer=NSTimer()
        //check old and new scores
        if self.high_score < self.old_score{
            writeToDocumentsFile(filename, value: String(high_score))
            self.old_score = self.high_score
            updateHighScoreLabel()
            //print("\(old_score) is the high score")
        }
    }
    
    //file handling function
    func writeToDocumentsFile(fileName:String,value:String) {
        
        let documentsPath = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)[0] as NSString!
        let path = documentsPath.stringByAppendingPathComponent(fileName)
        do {
            try value.writeToFile(path, atomically: true, encoding: NSUTF8StringEncoding)
        } catch let error as NSError {
            print("ERROR : writing to file \(path) : \(error.localizedDescription)")
        }
        
    }
    
    //file handling function
    func readFromDocumentsFile(fileName:String) -> String {
        let documentsPath = NSSearchPathForDirectoriesInDomains(.DocumentDirectory, .UserDomainMask, true)[0] as NSString
        let path = documentsPath.stringByAppendingPathComponent(fileName)
        var readText : String = ""
        //print(path)
        do {
            try readText = NSString(contentsOfFile: path, encoding: NSUTF8StringEncoding) as String
        }
        catch let error as NSError {
            print("ERROR : reading from file \(fileName) : \(error.localizedDescription)")
        }
        return readText
    }
    
    //reads old score from file and saves to memory
    func readOldScore(){
        let old = readFromDocumentsFile(filename)
        if (old != ""){
            self.old_score=Float(old)!
            //print ("\(old) is old")
        }
    }
    
    //updates high score label
    func updateHighScoreLabel(){
        if self.old_score < 999999{
            self.high_score_label.text = ("High Score: \(self.old_score)s")
        }
        else {
            self.high_score_label.text = ("High Score: 0.0s")
        }
    }
    
    //when share on twitter button is pressed
    @IBAction func twitterShareTap(sender: AnyObject) {
        if SLComposeViewController.isAvailableForServiceType(SLServiceTypeTwitter){
            let twitterSheet:SLComposeViewController = SLComposeViewController(forServiceType: SLServiceTypeTwitter)
            twitterSheet.setInitialText("I just scored a high score of \(self.old_score)s on Tapper!")
            self.presentViewController(twitterSheet, animated: true, completion: nil)
        } else {
            let alert = UIAlertController(title: "Accounts", message: "Please login to a Twitter account to share.", preferredStyle: UIAlertControllerStyle.Alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertActionStyle.Default, handler: nil))
            self.presentViewController(alert, animated: true, completion: nil)
        }
    }
    
}

