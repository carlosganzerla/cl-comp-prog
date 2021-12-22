(declaim (optimize (safety 0) (debug 0) (speed 3)))

(defun get-ans (n)
  (do ((i 0 (1+ i))
       (fst 1000001)
       (snd 1000001))
      ((>= i n) (+ fst snd))
      (let ((a (read)))
        (declare (fixnum a i n fst snd))
        (cond ((< a fst) (psetf fst a snd fst))
              ((< a snd) (setf snd a))))))

(declaim (inline get-ans))

(defun main ()
  (dotimes (_ (read))
    (format t "~A~%" (get-ans (read)))))

(main)
