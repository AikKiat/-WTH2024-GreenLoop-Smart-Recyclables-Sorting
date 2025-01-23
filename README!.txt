Hello!

The code file <<Final_Code_Recyclables_Detector>> is the final rendition of this AI-driven recyclables classification. 
In it, are some of the code lines derived from <<Serialcomm_Interface_test_VisualStudio>>, reformatted and compiled to merge into the main system.
The main system in <<Final_Code_Recyclables_Detector>> is thus as such:
-Using OpenCV to capture images of recyclables (image is captured every 5 seconds now, can be changed in code).
-Passing said image into one of the already exported, trained Tensorflow ML models under the file "Trained models".
-Once classification of the captured recyclable in the image has been reached, result is parsed through this same code file via Baud Rate 115200, COM Port 5 to an suitable Arduino UNO board that should already be connected.
-This connected board should have the .ino code file included in the "Serialcomm_interface_test_ArduinoBoardSketch" folder, uploaded to it.
-If this is done correctly, the Serial Monitor should print out the appropriate result that has just been sent over, via the same Baud Rate 115200, Com Port 5.

***Of course, both Baud Rate and COM Port can be changed according to the hardware configurations and connections of the UNO Board.