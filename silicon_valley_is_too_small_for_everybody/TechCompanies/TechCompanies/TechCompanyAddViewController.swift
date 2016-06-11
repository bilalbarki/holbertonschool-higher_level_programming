//
//  TechCompanyAddViewController.swift
//  TechCompanies
//
//  Created by Bilal Barki on 6/10/16.
//  Copyright © 2016 Bilal. All rights reserved.
//

import UIKit

class TechCompanyAddViewController: UIViewController {

    @IBOutlet weak var enterName: UITextField!
    @IBOutlet weak var enterTown: UITextField!
    @IBOutlet weak var enterImageName: UITextField!
    @IBOutlet weak var enterType: UITextField!
    @IBOutlet weak var addButton: UIButton!
    @IBOutlet weak var doneField: UILabel!
    var inputData: [String:String] = ["name": "", "town": "", "imageName": "", "type": ""]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.title = "Add Entry"
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    //on add button press
    @IBAction func tapAddButton(sender: AnyObject) {
        if let entered_name = enterName.text {
            if entered_name != "" {
                self.inputData["name"] = entered_name
            }
        }
        
        if let entered_town = enterTown.text {
            if entered_town != "" {
                self.inputData["town"] = entered_town
            }
        }
        
        if let entered_imageName = enterImageName.text {
            if entered_imageName != "" {
                self.inputData["imageName"] = entered_imageName
            }
        }
        
        if let entered_type = enterType.text {
            if entered_type != "" {
                self.inputData["type"] = entered_type
            }
        }
        if inputData["name"] != "" && inputData["town"] != "" && inputData["imageName"] != "" && inputData["type"] != "" {
            self.post(inputData, url: "http://173.246.108.142/ios/api.php")
        }
        
        self.enterName.text = ""
        self.enterTown.text = ""
        self.enterImageName.text = ""
        self.enterType.text = ""
        self.doneField.hidden = false
    }
    
    //makes a post request to the api and calls the append function
    func post(params : Dictionary<String, String>, url : String) {
        let name = params["name"]!.stringByAddingPercentEncodingWithAllowedCharacters(.URLHostAllowedCharacterSet())!
        let town = params["town"]!.stringByAddingPercentEncodingWithAllowedCharacters(.URLHostAllowedCharacterSet())!
        let imageName = params["imageName"]!.stringByAddingPercentEncodingWithAllowedCharacters(.URLHostAllowedCharacterSet())!
        let type = params["type"]!.stringByAddingPercentEncodingWithAllowedCharacters(.URLHostAllowedCharacterSet())!
    
        let request = NSMutableURLRequest(URL: NSURL(string: url)!)
        let session = NSURLSession.sharedSession()
        request.HTTPMethod = "POST"
        
        let myParams = "name=\(name)&town=\(town)&imageName=\(imageName)&type=\(type)"
        let postData = myParams.dataUsingEncoding(NSASCIIStringEncoding, allowLossyConversion: true)
        request.HTTPBody = postData
        
        request.addValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")
        
        let task = session.dataTaskWithRequest(request, completionHandler: {data, response, error -> Void in
            // handle error
            guard error == nil else { return }
            
            //print("Response: \(response)")
            //let strData = NSString(data: data!, encoding: NSUTF8StringEncoding)
            //print("Body: \(strData)")
            EntitiesHelper.to_json(data!, update: true)
            NSNotificationCenter.defaultCenter().postNotificationName("refreshMyTableView", object: nil)
            print("Added")
            /*let json: NSDictionary?
            do {
                json = try NSJSONSerialization.JSONObjectWithData(data!, options: .MutableLeaves) as? NSDictionary
            } catch let dataError {
                // Did the JSONObjectWithData constructor return an error? If so, log the error to the console
                print(dataError)
                let jsonStr = NSString(data: data!, encoding: NSUTF8StringEncoding)
                print("Error could not parse JSON: '\(jsonStr)'")
                // return or throw?
                return
            }*/
            
            
            // The JSONObjectWithData constructor didn't return an error. But, we should still
            // check and make sure that json has a value using optional binding.
            /*if let parseJSON = json {
                // Okay, the parsedJSON is here, let's get the value for 'success' out of it
                let success = parseJSON["success"] as? Int
                print("Succes: \(success)")
            }
            else {
                // Woa, okay the json object was nil, something went worng. Maybe the server isn't running?
                let jsonStr = NSString(data: data!, encoding: NSUTF8StringEncoding)
                print("Error could not parse JSON: \(jsonStr)")
            }*/
            
        })
        
        task.resume()
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
