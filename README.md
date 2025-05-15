# GreenLoop, Smart Recyclables Sorting

### Ever felt the spark of determination and zeal to recycle and give our dear Mother its few more seconds of life, only to be overwhelmed by tons of recyclables to eventually give up?
### Don't worry. We are not at fault here. The fault lies with the amount of categories we are constantly faced with in choosing to do the right thing and recycle.
### It is time, to recycle right!

## Introducing GreenLoop, a conceptual coding idea utilising an Computer Vision, to automate the recycling process

#### How this works:
<ul>
  <li>Using an existing Tensorflow model, integrating it with OpenCV to capture images every 5 seconds, after which these images (of recyclables) will be processed.</li>
  <li>Results sent to an onbaord Arduino /ESP32 via serial comm, and further programming conditionals can be made such as controlling mechanical parts and features, to sort recyclables properly.</li>
  <li>For instance, our final presentation product featured a conveyor belt <img src= "https://github.com/user-attachments/assets/25b022e9-52b9-4a11-9dff-7068afa8719b" style = "width: 4rem; height:4rem;"> belt and some servos to do the sorting.</li>
</ul>

### How to use:
<ul>
  <li>The code file *Final_Code_Recyclables_Detector is the final rendition of this AI-driven recyclables classification. </li>
  <li>In it, are some of the code lines derived from <Serialcomm_Interface_test_VisualStudio>, reformatted and compiled to merge into the main system.</li>
  <li>Once classification of the captured recyclable in the image has been reached, result is parsed through this same code file via Baud Rate 115200, COM Port 5 to an suitable Arduino UNO board that should already be connected.</li>
  <li>This connected board should have the .ino code file included in the "Serialcomm_interface_test_ArduinoBoardSketch" folder, uploaded to it.</li>
  <li>If this is done correctly, the Serial Monitor should print out the appropriate result that has just been sent over, via the same Baud Rate 115200, Com Port 5.</li>
</ul>

*Of course, both Baud Rate and COM Port can be changed according to the hardware configurations and connections of the UNO Board*

## Example:
![GREENLoop](https://github.com/user-attachments/assets/5e611638-bdb4-4308-9ff3-5be059a2abb5)
