//
//  MyTVAppItem.swift
//  Open and play
//
//  Created by Bilal Barki on 6/25/16.
//  Copyright © 2016 Bilal Barki. All rights reserved.
//

import UIKit

class MyTVAppItem: NSObject {
    var name:String
    var url_stream:String
    init(name: String, url_stream: String) {
        self.name = name
        self.url_stream = url_stream
    }
    
    func get_name() -> String {
        return self.name
    }
    
    func get_url_stream() -> String {
        return self.url_stream
    }
}
