//
//  ViewTime.swift
//  Right on Time
//
//  Created by Bilal Barki on 6/17/16.
//  Copyright © 2016 Bilal Barki. All rights reserved.
//

import UIKit

//variables used in clock, label is for digital and Clock is for analog
struct TimerVariables {
    static var Label:[UILabel] = []
    static var Clock:[UIImageView] = []
}

class ViewTime: UIView {
    
    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)
        self.backgroundColor = UIColor(red: 0.0, green: 0.0, blue: 0.0, alpha: 1.0) //choose background color, remove this line if you want to choose background color from storyboard
        
        //choose interface, whether analog or digital
        self.digital()
        //self.analog()   //for analog clock, the image view should be a square
    }
    
    //analog function that describes an analog clock
    func analog() {
        for value in ["clock", "hour", "minute", "second"] {
            let image = UIImage(named: value)
            let imageView = UIImageView(image: image!)
            TimerVariables.Clock.append(imageView)
                imageView.frame = CGRect(x: 0, y: 0, width: self.frame.size.width, height: self.frame.size.height)
            addSubview(imageView)
        }
        TimerVariables.Clock[2].transform = CGAffineTransformRotate(TimerVariables.Clock[2].transform, (CGFloat(MyTimerHelper.get_minute()) * 6.0 * CGFloat(M_PI)) / 180.0);
        NSTimer.scheduledTimerWithTimeInterval(1, target: self, selector: #selector(self.rotate), userInfo: nil, repeats: true)
    }
    
    //auto adjusts text size
    override func layoutSubviews() {
        if TimerVariables.Label.count == 2 {
            for i in 0...1 {
                TimerVariables.Label[i].adjustsFontSizeToFitWidth = true
            }
        }
    
    }
    
    //rotates analog clock hands
    func rotate() {
        var hour = CGFloat(MyTimerHelper.get_hour())
        let minute = CGFloat(MyTimerHelper.get_minute())
        let second = CGFloat(MyTimerHelper.get_second())
        
       if hour > 12.0 { //12 hour conversion
            hour = hour - 12.0
        }
        
        UIView.animateWithDuration(0.3, animations: {
            TimerVariables.Clock[3].transform = CGAffineTransformMakeRotation((second * 6.0 * CGFloat(M_PI)) / 180.0)
            TimerVariables.Clock[2].transform = CGAffineTransformMakeRotation(((minute + (second/60)) * 6.0 * CGFloat(M_PI)) / 180.0)
            TimerVariables.Clock[1].transform = CGAffineTransformMakeRotation(((hour + minute / 60) * 30.0 * CGFloat(M_PI)) / 180.0)
        })
    }
    
    //function that describes the digital clock
    func digital() {
        for _ in 0...1 {
            let label = UILabel(frame: CGRect(x: 0, y: 0, width: self.frame.size.width, height: self.frame.size.height))
            label.font = UIFont (name: "DSEG7ModernMini-Bold", size: self.frame.size.width / self.frame.size.height
                * 30)
            label.baselineAdjustment = .AlignCenters
            label.textAlignment  = NSTextAlignment.Center
            label.textColor = UIColor(red: 0.0, green: 1.0, blue: 0, alpha: 1.0)
            label.adjustsFontSizeToFitWidth = true
            TimerVariables.Label.append(label)
            addSubview(label)
        }
        self.update()
        TimerVariables.Label[1].alpha = 0.1
        TimerVariables.Label[1].text = "88:88:88"
        NSTimer.scheduledTimerWithTimeInterval(1, target: self, selector: #selector(self.update), userInfo: nil, repeats: true)
    }
    
    //updates time for digital clock after every second
    func update() {
        let hour = String(format: "%02d", MyTimerHelper.get_hour())
        let minute = String(format: "%02d", MyTimerHelper.get_minute())
        let second = String(format: "%02d", MyTimerHelper.get_second())
        TimerVariables.Label[0].text = "\(hour):\(minute):\(second)"
    }

    /*
    // Only override drawRect: if you perform custom drawing.
    // An empty implementation adversely affects performance during animation.
    override func drawRect(rect: CGRect) {
        // Drawing code
    }
    */

}


