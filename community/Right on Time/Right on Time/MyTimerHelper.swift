//
//  MyTimerHelper.swift
//  Right on Time
//
//  Created by Bilal Barki on 6/17/16.
//  Copyright © 2016 Bilal Barki. All rights reserved.
//

import Foundation

extension NSDate {
    func hour() -> Int {
        //Get Hour
        let calendar = NSCalendar.currentCalendar()
        let components = calendar.components(.Hour, fromDate: self)
        let hour = components.hour
        
        //Return Hour
        return hour
    }
    
    
    func minute() -> Int {
        //Get Minute
        let calendar = NSCalendar.currentCalendar()
        let components = calendar.components(.Minute, fromDate: self)
        let minute = components.minute
        
        //Return Minute
        return minute
    }
    
    func seconds() -> Int {
        //Get Minute
        let calendar = NSCalendar.currentCalendar()
        let components = calendar.components(.Second, fromDate: self)
        let minute = components.second
        
        //Return Minute
        return minute
    }
}

//describes getter functions for getting hour, minute, and second from the current time
class MyTimerHelper {
    
    static func get_hour() -> Int {
        let currentDate = NSDate()
        return currentDate.hour()
    }
    
    static func get_minute() ->Int {
        let currentDate = NSDate()
        return currentDate.minute()
    }
    
    static func get_second() -> Int {
        let currentDate = NSDate()
        return currentDate.seconds()
    }
}