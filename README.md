# Comb.Mod.SAQ.Pix

## Overview  
<img src="./ReadMeAssets/Images/Demo.png" width="50%">  
This is the current status of the "new" SAQ Model build. I have included field cage rings so that if needed, we can export the model to simulation.  
  
## Current Assets   
⚠️ - **[Pixel Combs](/1.KiCAD/Pixel.Combs):** ./1.KiCAD/Pixel.Combs  
<img src="./ReadMeAssets/Images/Pixel.Combs.png" width="50%">   
img updated: 5/12/2023   
Geometry:  
(Outer Radius) : 39 mm  
(Inner Radius) : 30 mm  
  
--------------  
⚠️ - **[Collection Board](/1.KiCAD/Feed.Through.Adapter/):** ./1.KiCAD/Feed.Through.Adapter  
**1-  Non-Metallic**  
<img src="./ReadMeAssets/Images/Readout.PCB.png" width="50%">  
The PCB Component of our collection component.  
**2.  Metallic**  
<img src="./ReadMeAssets/Images/Readout.Top.png" width="50%">  
<img src="./ReadMeAssets/Images/Readout.Bot.png" width="50%">  
  
__Combined__  
Top of readout adapter  
<img src="./ReadMeAssets/Images/Readout.1.png" width="50%">  
Bottom of readout adapter  
<img src="./ReadMeAssets/Images/Readout.Adapter.png" width="50%">  
  
<a href="https://www.digikey.com/en/products/detail/mill-max-manufacturing-corp/0906-1-15-20-75-14-11-0/1147049">Pogo Pins used for design [Digi-Key]</a>  
img updated: 5/15/2023  
  
--------------  
🟠 - **[Steel Vessel](/2.Fusion360/Vessel):** ./2.Fusion360/Vessel/Smooth.SAQ.Pix.Vessel.5.15.2023     
<img src="./ReadMeAssets/Images/Vessel.png" width="50%">   
img updated: 5/15/2023  
  
Vessel still needs to be changed for other feedthroughs. Similarly to the door will be a multiple outlet one on the side, and some at the top of the vessel.  
  
--------------- 
## Planned Development
📝 - Dummy Signal Board  
📝 - [19 Channel SAQ Board] or [2-Three Channel, 2-Four Channel, 1-Five Channel]  
📝 - Source Holder  

---------------  
  
### Instrunctions and Testing  
  
**[Channel Tester](/1.KiCAD/Channel.Tester/):** /1.KiCAD/Channel.Tester  
<img src="./ReadMeAssets/Images/Vessel.png" width="50%">   
  
::: The Channel Tester has the same dimensions of a pixel board :::  
1- Insert the Channel Tester board and secure it like a pixel board.  
2- Send test signals in a labeled slot, record the channel triggered  
  ex: Slot A receives input, channel 7 is triggered. -> A7  
3- When each letter has a number assigned, you can begin tests.  
  
  
  
  
  
  
  
  
---------------
|   Legend       |  Meaning                      |
|----------------|-------------------------------|
|📝| This component is in the design and illustration phase            |
|🟠| This component is under development            |
|⚠️| This component requires feedback before further development |
|🟡| This component files are under final review |
|🟢| This component is ready for production |

