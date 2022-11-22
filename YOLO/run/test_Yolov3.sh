if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ASL_data/obj.data cfg/yolov3.cfg backup/yolov3_final.weights < ASL_data/test.txt > results/Yolov3_test_cpu_results.txt
else
    ./darknet detector test ASL_data/obj.data cfg/yolov3.cfg backup/yolov3_final.weights < ASL_data/test.txt > results/Yolov3_test_results.txt
fi
