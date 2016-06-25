//
//  ViewController.swift
//  Open and play
//
//  Created by Bilal Barki on 6/25/16.
//  Copyright © 2016 Bilal Barki. All rights reserved.
//

import UIKit
import AVKit
import AVFoundation

class ViewController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource {

    @IBOutlet weak var collectionView: UICollectionView!
    var TVAppItems:[MyTVAppItem] = []
    let avPlayerViewController = AVPlayerViewController()
    var avPlayer:AVPlayer?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        TVAppItems.append(MyTVAppItem(name: "bip", url_stream: "http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8"))
        TVAppItems.append(MyTVAppItem(name: "Apple Keynote", url_stream: "http://qthttp.apple.com.edgesuite.net/1010qwoeiuryfg/sl.m3u8"))
        
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
        
    func collectionView(collectionView: UICollectionView, didUpdateFocusInContext context:UICollectionViewFocusUpdateContext,withAnimationCoordinator coordinator: UIFocusAnimationCoordinator) {
        
        if let previousIndexPath = context.previouslyFocusedIndexPath,
            let cell = collectionView.cellForItemAtIndexPath(previousIndexPath) {
            cell.contentView.layer.borderWidth = 0.0
        }
        
        if let indexPath = context.nextFocusedIndexPath,
            let cell = collectionView.cellForItemAtIndexPath(indexPath) {
            cell.contentView.layer.borderWidth = 8.0
            cell.contentView.layer.borderColor = UIColor.blackColor().CGColor
        }
    }
    
    func collectionView(collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return self.TVAppItems.count
    }

    func collectionView(collectionView: UICollectionView, cellForItemAtIndexPath indexPath: NSIndexPath) ->
        UICollectionViewCell {
        let cell = collectionView.dequeueReusableCellWithReuseIdentifier("cell", forIndexPath: indexPath) as! CollectionViewCell
        cell.titleLabel.text = self.TVAppItems[indexPath.row].get_name()
        return cell
    }
    
    
    func collectionView(collectionView: UICollectionView, didSelectItemAtIndexPath indexPath: NSIndexPath) {
        let movieURL = NSURL(string: TVAppItems[indexPath.row].get_url_stream())
        if let url = movieURL {
            self.avPlayer = AVPlayer(URL: url)
            self.avPlayerViewController.player = self.avPlayer
            self.presentViewController(self.avPlayerViewController, animated: true, completion: {self.avPlayerViewController.player?.play()})
        }
    }

}

