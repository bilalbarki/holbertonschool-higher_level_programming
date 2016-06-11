//
//  TechCompanyDetailViewController.swift
//  TechCompanies
//
//  Created by Bilal Barki on 6/8/16.
//  Copyright © 2016 Bilal. All rights reserved.
//

import UIKit

class TechCompanyDetailViewController: UIViewController {

    var entity:Entity! = nil
    @IBOutlet weak var label_entity: UILabel!
    @IBOutlet weak var image_entity: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
        if entity != nil {
            self.title = entity.getName()
            self.label_entity.text = entity.getTown()
            if entity.getimageName() == "spple" {
                self.image_entity.image = UIImage(named: "apple")
            }
            else if EntitiesHelper.images.contains(entity.getimageName()){
                self.image_entity.image = UIImage(named: entity.getimageName())
            }
            else {
                self.image_entity.image = UIImage(named: "404")
            }

        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()

        // Dispose of any resources that can be recreated.
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
