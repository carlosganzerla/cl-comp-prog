(defstruct (et (:conc-name nil) (:constructor %make-et)) 
  top bot side total)

(defun make-et (h)
  (%make-et :top 1 :bot (expt 2 h) 
                  :side (1+ h) :total (- (expt 2 (1+ h)) 2)))

(defun mirror-side (et)
  (incf (total et) (+ (total et) (side et)))
  (incf (bot et) (bot et))
  (incf (top et) (top et)))

(defun mirror-bot (et)
  (incf (total et) (+ (total et) (bot et)))
  (incf (side et) (side et))
  (setf (bot et) (top et)))

(defun mirror-top (et)
  (incf (total et) (+ (total et) (top et)))
  (incf (side et) (side et))
  (setf (top et) (bot et)))

(defun main ()
  (let ((et (make-et (read))))
    (dotimes (_ (read))
      (if (= (read) 2)
          (format t "~A~%" (mod (total et) 1000000007))
          (case (read)
            ((1 2) (mirror-side et))
            (3 (mirror-top et))
            (4 (mirror-bot et)))))))

(main)
