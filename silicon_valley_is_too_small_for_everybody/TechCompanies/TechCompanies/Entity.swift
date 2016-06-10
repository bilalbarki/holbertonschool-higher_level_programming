//
//  Entity.swift
//  TechCompanies
//
//  Created by Bilal Barki on 6/8/16.
//  Copyright © 2016 Bilal. All rights reserved.
//

import Foundation

enum EntityType:String {
    case None = "None"
    case School = "School"
    case TechCompany = "TechCompany"
}

class Entity {
    private var name:String
    private var town:String
    private var imageName:String
    private var type:EntityType
    
    init (name:String, town:String, imageName:String, type:EntityType = .None) {
        self.name = name
        self.town = town
        self.imageName = imageName
        self.type = type
    }
    
    func getName() -> String {
        return self.name
    }
    
    func getTown() -> String {
        return self.town
    }
    
    func getimageName() -> String {
        return self.imageName
    }
    
    func getType() -> EntityType {
        return self.type
    }
}