//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Bilal Barki on 6/8/16.
//  Copyright © 2016 Bilal. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {
    
    var schoolList:[Entity]!=[]
    var techCompanyList:[Entity]!=[]
    var sectionNames_0:[String] = ["Tech Companies", "Schools"]
    var sectionNames_1:[String] = ["San Francisco", "Mountain View", "Sunnyvale", "Cupertino"]
    let techDetailSegue = "techDetailSegue"
    var toggle: Bool = false
    
    
    var listOfSanFrancisco:[Entity]! = []
    var listOfMountainView:[Entity]! = []
    var listOfSunnyvale:[Entity]! = []
    var listOfCupertino:[Entity]! = []
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.title = "Entity list"
        EntitiesHelper.get_and_parse_json()
        NSNotificationCenter.defaultCenter().addObserver(self, selector: #selector(TechCompaniesListViewController.refreshList(_:)), name:"refreshMyTableView", object: nil)
        while techCompanyList.count == 0 {
            self.tableView.reloadData()
        }
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }
    
    //used in NSNotificationCenter for refreshing UI
    func refreshList(notification: NSNotification){
        techCompanyList = EntitiesHelper.getTechCompanies()
        schoolList = EntitiesHelper.getSchools()
        //self.tableView.contentInset = UIEdgeInsetsMake(20, 0, 0, 0);
        self.get_by_place()
        self.tableView.reloadData()
        
    }
    
    //updates by place list
    func get_by_place(){
        self.listOfSanFrancisco = EntitiesHelper.get_listOfSanFrancisco()
        self.listOfMountainView = EntitiesHelper.get_listOfMountainView()
        self.listOfSunnyvale = EntitiesHelper.get_listOfSunnyvale()
        self.listOfCupertino = EntitiesHelper.get_listOfCupertino()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // #warning Incomplete implementation, return the number of sections
        if toggle {
            return 4
        }
        else {
            return self.sectionNames_0.count
        }
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // #warning Incomplete implementation, return the number of rows
        if toggle {
            if section == 0 {
                return self.listOfSanFrancisco.count
            }
            else if section == 1 {
                return self.listOfMountainView.count
            }
            else if section == 2 {
                return self.listOfSunnyvale.count
            }
            else {
                return self.listOfCupertino.count
            }
        }
        else {
            return section == 0 ? self.techCompanyList.count : self.schoolList.count
        }
    }

    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)
        var entity:Entity
        // Configure the cell...
        if toggle {
            if indexPath.section == 0 {
                entity = self.listOfSanFrancisco[indexPath.row]
                
            }
            else if indexPath.section == 1 {
                entity = self.listOfMountainView[indexPath.row]
                
            }
            else if indexPath.section == 2 {
                entity = self.listOfSunnyvale[indexPath.row]
                
            }
            else {
                entity = self.listOfCupertino[indexPath.row]
            }
        }
        else {
            if indexPath.section == 0 {
                entity = self.techCompanyList[indexPath.row]
                
            }
            else{
                entity = self.schoolList[indexPath.row]
            }
        }
        cell.textLabel?.text = entity.getName()
        switch (entity.getType()) {
        case .School:
            cell.detailTextLabel?.text = "I love studying"
        default:
            cell.detailTextLabel?.text = "I love working"
        }
        
        if entity.getimageName() == "spple" {
            cell.imageView?.image = UIImage(named: "apple")
        }
        else if EntitiesHelper.images.contains(entity.getimageName()){
            cell.imageView?.image = UIImage(named: entity.getimageName())
        }
        else {
            cell.imageView?.image = UIImage(named: "404")
        }
        
        
        cell.imageView!.contentMode = UIViewContentMode.ScaleAspectFit
        let itemSize = CGSizeMake(30, 30);
        UIGraphicsBeginImageContextWithOptions(itemSize, false, UIScreen.mainScreen().scale);
        cell.imageView!.sizeToFit()
        let imageRect = CGRectMake(0.0, 0.0, itemSize.width, itemSize.height);
        cell.imageView?.image!.drawInRect(imageRect)
        cell.imageView?.image! = UIGraphicsGetImageFromCurrentImageContext();
        UIGraphicsEndImageContext();
        
        return cell
    }
    

    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        if toggle {
            return sectionNames_1[section]
        }
        else {
            return sectionNames_0[section]
        }
        /*switch(section){
            case 0: return sectionNames[0]
            case 1: return sectionNames[1]
            default: return ""
        }*/
    }
    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
       
        if toggle{
            if segue.identifier == techDetailSegue {
                let destVC = segue.destinationViewController as? TechCompanyDetailViewController
                let sectionSelected = tableView.indexPathForSelectedRow?.section
                let rowSelected = tableView.indexPathForSelectedRow?.row
                var list: [Entity]
                if sectionSelected == 0 {
                    list = self.listOfSanFrancisco
                }
                
                else if sectionSelected == 1 {
                    list = self.listOfMountainView
                }
                
                else if sectionSelected == 2 {
                    list = self.listOfSunnyvale
                }
                
                else {
                    list = self.listOfCupertino
                }
                
                destVC?.entity = list[rowSelected!]
            }
        }
        else {
            if segue.identifier == techDetailSegue {
                let destVC = segue.destinationViewController as? TechCompanyDetailViewController
                let sectionSelected = tableView.indexPathForSelectedRow?.section
                let rowSelected = tableView.indexPathForSelectedRow?.row
            
                let list = sectionSelected == 0 ? techCompanyList : schoolList
                destVC?.entity = list[rowSelected!]
            }
        }
    }
    
    //on toggle switches the toggle variable value and reloads UI
    @IBAction func toggleIt(sender: UIBarButtonItem) {
        toggle = toggle == false ? true : false
        self.tableView.reloadData()
    }
    
    
    
    

}
