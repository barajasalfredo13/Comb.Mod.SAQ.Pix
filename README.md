# Comb.Mod.SAQ.Pix
::: Important Notes :::  
In the following weeks I am planning on separating each interchangable component. Since some of the designs are final. When I generate the files, all the raw files and production files will be placed in one of two folders.  

::: Updates :::
- Designed, Modeled, and created Drawings for Pixel Tiles.  
- Labeled Pixel Tiles with Letter Codes so that they match the Stencil Codes.  
- Added Geometric and Material Informatioon to the readme.  
- ReOrganized Files so that they are separated by function type.  
- Minor Design Fixes  


## Overview  
<img src="./z.ReadMeAssets/Images/Demo.png" width="50%">  
This is the current status of the "new" SAQ Model build. I have included field cage rings so that if needed, we can export the model to simulation.  
  
## Current Assets   
🟡 - **[Pixel Combs](/Modular.Pixel.Combs/):** ./Modular.Pixel.Combs/  
<img src="./z.ReadMeAssets/Images/Pixel.Combs.png" width="50%">     
:: Base Geometry and Dimensions ::  
(Outer Radius) : 39 mm  
(Inner Radius) : 30 mm  
PCB.Dimensions : 78 mm x 78 mm  
Pixel Pitch : 10 mm  
  
Descriptions :::  
A- Solid Single Conductive Plane Hexagon  
B- Solid Single Conductive Plane Hexagon with Single Biased Hexagon Ring  
C- Solid Single Circular Plane with Single Biased Hexagon Ring  
  
::: Intended Use :::  
Pixel Comb planes were designed to be used as experimental collection planes for specific interactions. With use of shadow masks, we can deposite materials to experimentally test. measure and characterize novel materials.  
  
Note: Currently Pixel Combs have Sharp edges on the hexagons. This will change to Soft Edges so that the Shadow Masks have a perfect fit.  
  
--------------  
🟡 - **[PCB Readout Feedthrough](/Readout.Feed.Through.Adapter/):** ./Readout.Feed.Through.Adapter/  
**1-  Non-Metallic**  
<img src="./z.ReadMeAssets/Images/Readout.PCB.png" width="50%">  
The PCB Component of our collection component.  
**2.  Metallic**  
<img src="./z.ReadMeAssets/Images/Readout.Top.png" width="50%">  
<img src="./z.ReadMeAssets/Images/Readout.Bot.png" width="50%">  
  
__Combined__  
Top of readout adapter  
<img src="./z.ReadMeAssets/Images/Readout.1.png" width="50%">  
Bottom of readout adapter  
<img src="./z.ReadMeAssets/Images/Readout.Adapter.png" width="50%">  

<a href="https://www.digikey.com/en/products/detail/mill-max-manufacturing-corp/0906-1-15-20-75-14-11-0/1147049">Pogo Pins used for design [Digi-Key]</a>  
img updated: 5/15/2023  
  
--------------  
🟠 - **[Steel Vessel](/Vessel.Full/Fusion360/):** ./2.Fusion360/Vessel/Smooth.SAQ.Pix.Vessel.5.15.2023     
<img src="./z.ReadMeAssets/Images/Vessel.png" width="50%">   
img updated: 5/15/2023  
  
Vessel will be modified so that Standardized Feedthroughs can be used.   
  
--------------- 
## Planned Development
📝 - [19 Channel SAQ Board] or [2-Three Channel, 2-Four Channel, 1-Five Channel]  
📝 - Source Holder   
  
  
---------------  
### Research and Development Tools ###
✨🟠 - **[Pixel Shadow Masks](/Shadow.Mask.Kit/Fusion360/) ./Shadow.Mask.Kit/Fusion360/  
    
  Material ::: 316L Stainless Steel   
  Shadow Mask Thickness ::: [ 0.015 in // 0.381 mm ]  
    
<img src="./z.ReadMeAssets/Images/Shadow.Mask.Kit.png" width="50%"> 
316L Stainless Steel was chosen due to its low outgassing and resistiveness to corrosion  
  
----------------  
### Instructions and Testing  
  
✨🟡- **[Channel Tester](/Channel.Tester/KiCAD/):** ./Channel.Tester/KiCAD  
<img src="./z.ReadMeAssets/Images/Channel.Tester.png" width="50%">   
  
::: The Channel Tester has the same dimensions of a pixel board :::  
1- Insert the Channel Tester board and secure it like a pixel board.  
2- Send test signals in a labeled slot, record the channel triggered  
  ex: Slot A receives input, channel 7 is triggered. -> A7  
3- When each letter has a number assigned, you can begin tests.  
  
  
---------------
|   Legend       |  Meaning                      |
|----------------|-------------------------------|
|✨| Recently Added / New Items            |
|📝| This component is in the design and illustration phase            |
|🟠| This component is under development            |
|⚠️| This component requires feedback before further development |
|🟡| This component files are under final review |
|🟢| This component is ready for production |

