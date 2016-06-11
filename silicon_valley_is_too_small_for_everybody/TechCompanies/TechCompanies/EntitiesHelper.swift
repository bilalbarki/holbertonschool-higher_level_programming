//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Bilal Barki on 6/8/16.
//  Copyright © 2016 Bilal. All rights reserved.
//

import Foundation

class EntitiesHelper {
    static var listOfSchool:[Entity]! = []
    static var listOfTechCompany:[Entity]! = []
    
    static var listOfSanFrancisco:[Entity]! = []
    static var listOfMountainView:[Entity]! = []
    static var listOfSunnyvale:[Entity]! = []
    static var listOfCupertino:[Entity]! = []
    static var images:[String] = ["apple", "docker", "google", "holberton", "linkedin", "twitter", "yahoo"]
    
    //returns schools
    static func getSchools() -> [Entity]! {
        /*if listOfSchool.count == 0 {
            listOfSchool.append(Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School))
        }*/
        return listOfSchool
    }
    
    //returns tech companies
    static func getTechCompanies() -> [Entity]!{
        /*if listOfTechCompany.count == 0 {
            listOfTechCompany.append(Entity(name: "Linkedin", town: "San Francisco", imageName: "linkedin", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Docker", town: "San Francisco", imageName: "docker", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Google", town: "Mountain View", imageName: "google", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
            
        }*/
        
        return listOfTechCompany
    }
    
    //sorts by place, just for initialization
    static func sortByPlace() {
        for item in listOfSchool + listOfTechCompany {
                append_it(item)
        }
    }
    
    //appends element to appropriate list
    static func append_it(item: Entity) {
        if item.getTown() == "San Francisco" || item.getTown() == "San Franscico" { //because of mistake in the api
            listOfSanFrancisco.append(item)
        }
        else if item.getTown() == "Mountain View" {
            listOfMountainView.append(item)
        }
        else if item.getTown() == "Sunnyvale" {
            listOfSunnyvale.append(item)
        }
        else if item.getTown() == "Cupertino" {
            listOfCupertino.append(item)
        }
    }
    
    static func get_listOfSanFrancisco() -> [Entity] {
        return listOfSanFrancisco
    }
    
    static func get_listOfMountainView() -> [Entity] {
        return listOfMountainView
    }
    
    static func get_listOfSunnyvale() -> [Entity] {
        return listOfSunnyvale
    }
    
    static func get_listOfCupertino() -> [Entity] {
        return listOfCupertino
    }
    
    //converts to json and appends to appropriate list
    static func to_json(data: NSData, update: Bool) {
        
        let json = try! NSJSONSerialization.JSONObjectWithData(data, options:.MutableLeaves)
        if !update {
            for index in 0...json.count-1 {
                if let name = json[index]["name"] as? String {
                    if let town = json[index]["town"] as? String {
                        if let imageName = json[index]["imageName"] as? String {
                            if let type = json[index]["type"] as? String {
                                if type == "TechCompany" {
                                    listOfTechCompany.append(Entity(name: name, town: town, imageName: imageName, type: EntityType(rawValue: type)!))
                                }
                                else if type == "School" {
                                    listOfSchool.append(Entity(name: name, town: town, imageName: imageName, type: EntityType(rawValue: type)!))
                                }
                            }
                        }
                    }
                }
            }
            sortByPlace()
        }
        else {
            let index = json.count - 1
            if let name = json[index]["name"] as? String {
                if let town = json[index]["town"] as? String {
                    if let imageName = json[index]["imageName"] as? String {
                        if let type = json[index]["type"] as? String {
                            if type == "TechCompany" {
                                let temp = Entity(name: name, town: town, imageName: imageName, type: EntityType(rawValue: type)!)
                                listOfTechCompany.append(temp)
                                append_it(temp)
                            }
                            else if type == "School" {
                                let temp = Entity(name: name, town: town, imageName: imageName, type: EntityType(rawValue: type)!)
                                listOfSchool.append(temp)
                                append_it(temp)
                            }
                        }
                    }
                }
            }
        }
    }
    
    //gets json, parses it and calls the appropriate function to append
    static func get_and_parse_json() {
        let url = "http://173.246.108.142/ios/api.php"
        let requestURL: NSURL = NSURL(string: url)!
        let task = NSURLSession.sharedSession().dataTaskWithURL(requestURL) {(data, response, error) in
            let httpResponse = response as! NSHTTPURLResponse
            let statusCode = httpResponse.statusCode
            
            if (statusCode == 200) {
                to_json(data!, update: false)
                NSNotificationCenter.defaultCenter().postNotificationName("refreshMyTableView", object: nil)
            }
            
        }
        
        task.resume()
    }
    
    

}