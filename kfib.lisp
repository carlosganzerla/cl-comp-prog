(declaim (optimize (safety 0) (debug 0) (speed 3)))

(defun kfib (n k)
  (let ((vec (make-array n :element-type 'fixnum
                         :initial-element 1)))
    (do ((i k (1+ i))
         (j 0 (1+ j))
         (current k (mod (- (* 2 current) (aref vec j)) 1000000007)))
        ((>= i n) (aref vec (1- n)))
        (declare (fixnum i j k n current))
        (setf (aref vec i) current))))

(declaim (inline kfib))

(defun main ()
  (format t "~A~%" (kfib (read) (read))))

(main)
