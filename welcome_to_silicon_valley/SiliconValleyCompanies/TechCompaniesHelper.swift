//
//  TechCompaniesHelper.swift
//  SiliconValleyCompanies
//
//  Created by user118475 on 5/29/16.
//  Copyright © 2016 Bilal. All rights reserved.
//

import Foundation

class TechCompaniesHelper{
    static var companies:[String] = ["Holberton", "Linkedin", "Docker", "Google", "Yahoo", "Apple"]
    static func getTechCompanies() -> [String]{
        return companies
    }
}