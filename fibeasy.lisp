(declaim (optimize (speed 3) (safety 0) (debug 0)))

(defun main ()
  (dotimes (x (read))
    (let ((input (floor (log (read) 2))))
      (format t "~A~%" (cond ((>= 1 input) input)
                             ((= (mod input 4) 1) 9)
                             (t (mod input 4)))))))

(dotimes (x 10000) (print x))
