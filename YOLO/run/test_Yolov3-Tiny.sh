if [ "$1" = "-cpu" ] ; then
    ./darknet -nogpu detector test ASL_data/obj.data cfg/yolov3-tiny.cfg backup/yolov3-tiny_final.weights < ASL_data/test.txt > results/Yolov3-Tiny_test_cpu_results.txt
else
    ./darknet detector test ASL_data/obj.data cfg/yolov3-tiny.cfg backup/yolov3-tiny_final.weights < ASL_data/test.txt > results/Yolov3-Tiny_test_results.txt
fi
